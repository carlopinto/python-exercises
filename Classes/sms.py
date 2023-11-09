### Create a new class, SMS_store. The class will instantiate SMS_store objects, 
### similar to an inbox or outbox on a cellphone.
### This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages). 
### Each message will be represented as a tuple:
###     (has_been_viewed, from_number, time_arrived, text_of_SMS) 
###
### Write the class, create a message store object, write tests for these methods, and implement the methods.

class SMS():

    def __init__(self, viewed = False, from_num = "", time_arr = "", text = ""):
        self.has_been_viewed = viewed
        self.from_number = from_num
        self.time_arrived = time_arr
        self.text_of_sms = text
    

class SMS_store():

    def __init__(self, l=[]):
        """"""
        self.l = l

    def add_new_arrival(self,from_num, time_arr, text):
        """ 
            Makes new SMS tuple, inserts it after other messages
            in the store. When creating this message, its
            has_been_viewed status is set False.
        """
        new_sms = SMS(False, from_num, time_arr, text)
        self.l.append(new_sms)

    def message_count(self):
        """ Returns the number of sms messages in my_inbox """
        return len(self.l)
    
    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages """
        indexes = []
        for (i,m) in enumerate(self.l):
            if type(m) is SMS:
                if not m.has_been_viewed:
                    indexes.append(i)

        return indexes
    
    def get_message(self, i):
        """
            Return (from_number, time_arrived, text_of_sms) for message[i]
            Also change its state to "has been viewed".
            If there is no message at position i, return None
        """
        if i in range(len(self.l)):
            m = self.l[i]
            m.has_been_viewed = True
            return m.from_number, m.time_arrived, m.text_of_sms
        else:
            return None
        
    def delete(self, i):
        """ Delete the message at index i """
        if i in range(len(self.l)):
            self.l.pop(i)
            print("Message at index {0} deleted!".format(i))


    def clear(self):
        """ Delete all messages from inbox """
        self.l.clear()
        # print("Inbox cleared.")