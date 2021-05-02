# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.
class Phone:
    def __init__(self,phone_number):
        self.phone_number=phone_number
        self.call_history=[]
        self.message_history=[]
# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.
    def make_call(self,other_phone):
        call={}  
        call["to"]=other_phone.phone_number
        call["from"]=self.phone_number
        print(f"You called {other_phone.phone_number}.")
        self.call_history.append(call)
# Add a method called show_call_history. This method should print the call_history.
    def show_call_history(self):
        for number in self.call_history:
            print(number)
# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to
# from
# content
    def send_message(self,other_phone,message_text):
        message={}
        message["to"]=other_phone.phone_number
        message["from"]=self.phone_number
        message["content"]=message_text 
        self.message_history.append(message)
        other_phone.message_history.append(message)
# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self, number)
    def show_outgoing_messages(self):
        print("Outgoing Messages: ")
        for item in self.message_history:
            if item["from"]==self.phone_number:
                print(f"You wrote {item['content']} to {item['to']}")
    def show_incoming_messages(self):
        print("Incoming Messages: ")
        for item in self.message_history:
            if item["to"]==self.phone_number:
                print(f"You received {item['content']} from {item['from']}")
# Test your code !!!

fay=Phone("0549877253")
elisheva=Phone("0549877252")
ezra=Phone("0586523761")
mom=Phone("0587808157")
dad=Phone("0587808158")

fay.send_message(ezra,"Call me!!")
ezra.send_message(fay,"Busy right now, maybe later")
fay.send_message(elisheva, "What do you want for dinner?")
elisheva.send_message(fay, "Ravioli and salad please!")
mom.send_message(fay, "When do you need me to babysit?")
fay.send_message(mom, "Tomorrow at 4")
fay.send_message(dad, "Why isn't mom answering her phone?")

fay.show_outgoing_messages()
fay.show_incoming_messages()