from flask import Flask
from flask import send_file
from flask import request
from flask import render_template
from flask import jsonify, abort
from recommend.Recommend import Evaluation
from utils.movie_kind_index_converter import movie_kind_to_index
from utils.get_image_url import get_image_url
from utils.get_random_num import get_random_num
import json
import os
import hashlib
import pymysql

MYSQL_HOST = '47.106.98.20'
MYSQL_PORT = 23306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'Dowhatgroup'
MYSQL_DB_NAME = 'recommend'
MYSQL_TABLE_NAME = 'movie'


app = Flask(__name__)


@app.route('/')
def index():
    return send_file('static/1/html/1.html')


@app.route('/music')
def music():
    return send_file('static/bgm/music.html')


@app.route('/main.html')
def main():
    return send_file('static/2/index.html')


@app.route('/branch.html', methods=['post', 'get'])
def branch():
    if request.method == 'GET':
        token = request.args.get('tk')
        for root, dirs, files in os.walk("static/data/", topdown=False):
            if token in files:
                # db_operation
                db_conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, db=MYSQL_DB_NAME, user=MYSQL_USER,
                                          passwd=MYSQL_PASSWD, charset='utf8')
                db_cur = db_conn.cursor()
                sql = 'select * from movie'
                db_cur.execute(sql)

                movies = db_cur.fetchall()
                grade_giver = Evaluation('static/data/%s'%token, mood_rule_path = 'recommend/mood.json', gender_rule_path='recommend/gender.json')
                general_map = dict()
                for i in range(len(movies)):
                    movie = movies[i]
                    movie_kind_index = movie_kind_to_index(json.loads(movie[2]), 'static/movie-kind-to-index.json')
                    age_distance = abs(2018 - int(movie[3]))
                    general_map[str(i)] = grade_giver.FinalScore(movie_label=movie_kind_index, movie_age=age_distance, movie_rate=float(movie[1]) if movie[1]!="" else 0, para={'mood': 0.47 , 'age': 0.03, 'gender': 0.45, 'rate': 0.05})
                
                random_index_list = get_random_num()
                general_movie_rank = sorted(zip(general_map.values(), general_map.keys()), reverse=True)
                movie_rank = []
                for index in random_index_list:
                    movie_rank.append(general_movie_rank[index])
                info = dict()
                for j in range(1, 10):
                    selected_movie = movies[int(movie_rank[j -1][1])]
                    info['pic%d' % j] = get_image_url('static/movies.json', selected_movie[0])
                    info['fun_name%d' % j] = selected_movie[0]
                    info['date%d' % j] = selected_movie[3]
                    q = len(json.loads(selected_movie[4])) if len(json.loads(selected_movie[4])) <= 5 else 5
                    info['introduction%d' % j] = ', '.join(json.loads(selected_movie[4])[:q])
                db_conn.commit()
                db_conn.close()
                os.system('nohup python3 utils/kill.py --path %s'%'static/data/%s >/dev/null 2>&1 & \n\n'%token)
                return render_template('index.html', info=info)
            else:
                return abort(404)
    else:
        return abort(404)


@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')


@app.route('/deliver', methods=['post', 'get'])
def test():
    if request.method == 'POST':
        img = request.form['image']
        md5 = hashlib.md5()
        md5.update(img.encode("utf-8"))
        token = md5.hexdigest()
        os.system("touch static/data/" + token)
        with open("static/data/" + token, 'w+') as f:
            f.write(img)
            f.close()
        return token
    else:
        return abort(404)


@app.route('/emotion', methods=['post', 'get'])
def deliver():
    emotion = request.args.get('emotion')
    print(emotion)
    return jsonify({'emotion': emotion})


@app.route('/static/data/<token>')
def refuse(token):
    abort(404)


if __name__ == '__main__':
    app.run()
