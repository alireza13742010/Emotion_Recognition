def translaor(text):
  lan_detected = language_detector(text)
  if lan_detected == "PERSIAN":
    translator_persian = EasyGoogleTranslate(source_language='fa',target_language='en',timeout=10)
    out = translator_persian.translate(text)
  if lan_detected == "GERMAN":
    translator_germany = EasyGoogleTranslate(source_language='ge',target_language='en',timeout=10)   
    out = translator_germany.translate(text)
  if lan_detected == "SPANISH":
    translator_espanish = EasyGoogleTranslate(source_language='es',target_language='en',timeout=10) 
    out = translator_espanish.translate(text)  
  if lan_detected == "FRENCH":
    translator_french = EasyGoogleTranslate(source_language='fr',target_language='en',timeout=10) 
    out = translator_french.translate(text)     
  if lan_detected == "AFRIKAANS":
    translator_afrikans = EasyGoogleTranslate(source_language='af',target_language='en',timeout=10) 
    out = translator_afrikans.translate(text)     
  if lan_detected == "ARABIC":
    translator_arabic = EasyGoogleTranslate(source_language='ar',target_language='en',timeout=10) 
    out = translator_arabic.translate(text)   
  if lan_detected == "ARMENIAN":
    translator_armenian = EasyGoogleTranslate(source_language='hy',target_language='en',timeout=10) 
    out = translator_armenian.translate(text) 
  return  out, lan_detected       
