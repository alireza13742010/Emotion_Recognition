def language_detector(text):
  languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH, Language.PERSIAN, Language.AFRIKAANS, Language.ARABIC,  Language.ARMENIAN]
  detector = LanguageDetectorBuilder.from_languages(*languages).build()
  language = detector.detect_language_of(text)
  _ , lan = str(language).split('.')
  return lan
