#계정 설정 - 보안 - 보안 수준이 낮은 앱의 엑세스 허용
#gmail 설정 - IMAP 사용
import smtplib
#MIME 타입으로 변경시키기 위하여 import
from email.message import EmailMessage

SMT_SERVER = "smtp.gmail.com"

#gmail에서 지정한 포트번호
SMT_PORT = 465
message = EmailMessage()

#content 에 들어가기에 set_content 로
message.set_content("코드라이언 수업 중입니다.")

#헤더 부분에 들어감
message["Subject"] = "이것은 제목입니다."
message["From"] = "#########@gmail.com"
message["To"] = "#########@gmail.com"

smtp = smtplib.SMTP_SSL(SMT_SERVER,SMT_PORT)
smtp.login("#########@gmail.com","#####")
smtp.send_message(message)
smtp.quit()

