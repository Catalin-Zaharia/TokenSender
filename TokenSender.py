import smtplib, ssl, getpass, random
from email.message import EmailMessage

def sendToken():
    msg=EmailMessage()
    msg['From']=myemail
    msg['Subject']="Token evaluare"
    msg['To']=studentList[i]
    msg.set_content('Grupa 142\n\n'+tokenList[i]+'\n\nValabil pana la \n\nhttp://evaluare.fmi.unibuc.ro')
    return msg.as_string()

tokenList=open("tokenList.txt", "r").read().splitlines()
studentList=open("studentList.txt", "r").read().splitlines()
history = open ('history.txt', 'w')
for i in studentList:
    i.replace(" ", "")
for i in tokenList:
    i.replace(" ", "")
random.shuffle(studentList)
random.shuffle(tokenList)
myemail = input("Gmail-ul de pe care trimiti(merge si my.fmi), pentru default din fisier apasa enter: ") or open("defaultMail.txt","r").read()
print ("\nEmail-ul de pe care se vor trimite codurile: "+myemail+"\n")
print ("Pentru a folosi script-ul trebuie sa permiti folosirea aplicatiilor mai putin sigure pe contul de pe care trimiti\n\n"+
        "https://myaccount.google.com/u/0/lesssecureapps\n")
password=getpass.getpass(prompt="Parola(fara echo, nu se vede inputul): ", stream=None)

port = 465
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(myemail, password)
    for i in range(len(studentList)):
        server.sendmail(myemail, studentList[i], sendToken())
        print("Trimis la "+studentList[i])
        history.write("Trimis "+tokenList[i]+' la '+studentList[i]+'\n')

history.write('\n')
history.close()