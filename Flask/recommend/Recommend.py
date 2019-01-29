# -*- coding: utf-8 -*-
import json
import os


class MoodScore():
    def __init__(self, mood, mood_rule_path='mood.json'):
        file = open(mood_rule_path, 'r')
        js = file.read()
        self.__mood_rule = json.loads(js)
        self.__mood = mood
        file.close()

    def GiveScore(self, movie_label):
        self.__score = 0
        for key in self.__mood:
            self.__score += float(self.__mood[key]) * float(self.__mood_rule[str(key) + '-' + str(movie_label)])
        return self.__score

    def PrintScore(self):
        print(self.__score)


class GenderScore():
    def __init__(self, gender, gender_rule_path='gender.json'):
        file = open(gender_rule_path, 'r')
        js = file.read()
        self.__gender_rule = json.loads(js)
        self.__gender = gender
        file.close()

    def GiveScore(self, movie_label):
        self.__score = 0
        for key in self.__gender:
            size = 0
            score = 0
            for label in movie_label:
                size += 1
                score += float(self.__gender[key]) * float(self.__gender_rule[str(key) + '-' + str(label)])
            self.__score += score / size
        return self.__score

    def PrintScore(self):
        print(self.__score)


class AgeScore():
    def __init__(self, age):
        self.__age = 0
        for key, value in age.items():
            self.__age += float(key) * float(value)

    def GiveScore(self, movie_age):
        delta = self.__age - movie_age
        self.__score = 1 * (50 - abs(delta - 15)) / 50
        if self.__score < 0:
            self.__score = 0
        return self.__score

    def PrintScore(self):
        print(self.__score)


class Evaluation():
    def __init__(self, path, mood_rule_path='mood.json', gender_rule_path='gender.json'):
        file = open(path, 'r')
        js = file.read()
        data = json.loads(js)
        self.__mood = MoodScore(data[0], mood_rule_path)
        self.__age = AgeScore(data[1])
        self.__gender = GenderScore(data[2], gender_rule_path)
        file.close()

    def FinalScore(self, movie_label, movie_age, movie_rate, para):
        score = 0
        size = 0
        for i in movie_label:
            score += self.__mood.GiveScore(i)
            size += 1
        if size == 0:
            os.system('touch error_case')
            with open('error_case', 'w+') as f:
                f.write(json.dumps(movie_label))
                f.write(json.dumps(movie_rate))
                f.write(json.dumps(movie_age))
                f.close()
        score /= size
        score *= para['mood']
        score += self.__age.GiveScore(movie_age) * para['age']
        score += self.__gender.GiveScore(movie_label) * para['gender']
        score += float(movie_rate) / 10 * para['rate']
        return score
