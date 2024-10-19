def lable_prediction(prediction):
  scores = []
  for x in prediction[0]:
    scores.append(x['score'])
  idx = np.argmax(scores)
  return prediction[0][idx]['label']  
