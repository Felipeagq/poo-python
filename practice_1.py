import json
from typing import Optional

class Email:
    from2: list = []
    subject: Optional[str] =  None
    body: Optional[str] = None
    
    def changeSubject(self,subject:str) -> None:
        self.subject = subject
        
    def changeBody(self, body:str) -> None:
        self.body = body


class Gmail: 
    name = "Gmail"

class Hotmail:
    name = "Hotmail"


class EmailManagment:
    emailProvider: Optional[str] = None
    
    def send(self, to:list, text:str) -> int:
        emails = ",".join(to)
        print(f"email to{emails}\n{text}\nfrom{self.emailProvider.name}")
        return 1
    
    def checkInBox(self)-> list:
        emails: list = []
        for i in range(3):
            emailTmp = Email()
            emailTmp.from2 = [f"email{i}@email1.com",f"email{i}@email2.com"]
            emailTmp.changeSubject(f"subject {i}")
            emailTmp.changeBody(f"body {i}")
            emails.append(emailTmp)
        return emails

if __name__ == "__main__":
    gestor_correos = EmailManagment()
    gestor_correos.emailProvider = Gmail()
    emailss = gestor_correos.checkInBox()
    print(json.dumps(
        emailss, 
        default= lambda obj: obj.__dict__,
        sort_keys=True,
        indent=2
    ))