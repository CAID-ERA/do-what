let upload = document.getElementById("upload");
let imgElement = document.getElementById('avatar');
let station = document.getElementById('canvas1');

const EMO_MODEL_URL = 'static/2/model/emotion/model.json';
const AGE_MODEL_URL = 'static/2/model/age/model.json';
const GENDER_MODEL_URL = 'static/2/model/gender/model.json';


function cut(x, y, w, h){
  let src = cv.imread('avatar');
  let dst = new cv.Mat();
  let rect = new cv.Rect(x, y, w, h);
  dst = src.roi(rect);
  cv.imshow('canvas1', dst);
  src.delete();
  dst.delete();
}

async function recog_emo(canvasElement){
  const emotion_model = await tf.loadModel(EMO_MODEL_URL);
  const face_origin = tf.fromPixels(canvasElement, depth=1);
  const face_rescaled = tf.image.resizeBilinear(face_origin, [48, 48]);
  const face = tf.expandDims(face_rescaled, 0);
  const emo_prediction = emotion_model.predict(face.toFloat()).dataSync();
  console.log("EMOTION:");
  console.log(emo_prediction);
  return emo_prediction;
}

async function recog_age(canvasElement){
  const age_model = await tf.loadModel(AGE_MODEL_URL);
  const face_1_origin = tf.fromPixels(canvasElement, depth=1);
  const face_1_rescaled = tf.image.resizeBilinear(face_1_origin, [64, 64]);
  const face_1 = tf.expandDims(face_1_rescaled, 0);
  const age_prediction = age_model.predict(face_1.toFloat());
  console.log("AGE:");
  return await age_prediction.data()
}

async function recog_gender(canvasElement){
  const gender_model = await tf.loadModel(GENDER_MODEL_URL);
  const face_2_origin = tf.fromPixels(canvasElement, depth=3);
  const face_2_rescaled = tf.image.resizeBilinear(face_2_origin, [48, 48]);
  const face_2 = tf.expandDims(face_2_rescaled, 0);
  const gender_prediction = gender_model.predict(face_2.toFloat());
  console.log("GENDER:");
  return await gender_prediction.data()
}

async function recog(station){
  emo = await recog_emo(station);
  age = await recog_age(station);
  gender = await recog_gender(station);
  console.log(emo);
  console.log(age);
  console.log(gender);
  let general_result = [emo, age, gender];
  console.log("PREDICTION FINISHED");
  console.log(general_result);
  return general_result;
}

async function send(station){
  let data = await recog(station);
  console.log(JSON.stringify(data));
  $.post("/deliver", {image: JSON.stringify(data)}, function(token){
    next_url = "/branch.html?tk=" + token;
    window.location.href = next_url;
  })
}

upload.onclick = function(e){
  console.log("NICE");
  e.preventDefault();
  let tracker = new tracking.ObjectTracker(['face']);
  tracker.setStepSize(1.7);
  tracking.track('#avatar', tracker);
  console.log("A");
  tracker.on('track', function(event){
      event.data.forEach(function(rect){
      console.log("B");
      cut(rect.x, rect.y, rect.width, rect.height);
      console.log("C");
    });
  send(station);
  });
};
