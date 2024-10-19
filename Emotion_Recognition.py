def Emotion_detection(text):
  Language_detect ={"PERSIAN":"fa", "GERMAN":"ge", "SPANISH": "es",
                  "FRENCH":"fr", "AFRIKAANS":"af", "ARABIC":"ar",
                  "ARMENIAN": "hy"}
  tex,lan_detected = translaor(text)
  classifier = pipeline("text-classification",model='bhadresh-savani/bert-base-uncased-emotion', return_all_scores=True)
  prediction = classifier(tex)
  Emotion_out = lable_prediction(prediction)
  translator_general = EasyGoogleTranslate(source_language='en',target_language=Language_detect[lan_detected],timeout=10) 
  Emotion_out_language = translator_general.translate(Emotion_out) 
  return Emotion_out_language
