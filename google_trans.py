from googletrans import Translator

translator = Translator()
sentence = input("언어를 감지할 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요?")
detected = translator.detect(sentence)
result = translator.translate(sentence,dest)

print("=======출 력 결 과 ==========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("============================")