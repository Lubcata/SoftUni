class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    data = input()
    if data == "Stop":
        break
    token = data.split()
    sender = token[0]
    receiver = token[1]
    content = token[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(", ")))
for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())






