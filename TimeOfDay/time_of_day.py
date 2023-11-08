### Class to record the time of day

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs 
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """
        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs   
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60    

    def __str__(self):
        days = self.hours // 24
        if self.hours < 0 or self.hours > 23:
            hours = self.hours % 24
            return "{0:02d}:{1:02d}:{2:02d} ({3})".format(hours, self.minutes, self.seconds, days)
        else:
            return "{0:02d}:{1:02d}:{2:02d}".format(self.hours, self.minutes, self.seconds)
    
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
    
    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())
    
    def __ge__(self, other):
        """Greater than or equal to"""
        return self.to_seconds() >= other.to_seconds()
    
    def __gt__(self, other):
        """Greater than"""
        return self.to_seconds() > other.to_seconds()
    
    def __le__(self, other):
        """Less than or equal to"""
        return self.to_seconds() <= other.to_seconds()

    def __lt__(self, other):
        """Less than"""
        return self.to_seconds() < other.to_seconds()
    
    def __eq__(self, other):
        """Equal to"""
        return self.to_seconds() == other.to_seconds()
    
    def __ne__(self, other):
        """Not equal to"""
        return self.to_seconds() != other.to_seconds()
    
    def increment(self, seconds):
        self.__init__(0, 0, self.to_seconds() + seconds)

    def to_seconds(self):
        """ Return the number of seconds represented 
            by this instance 
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def between(self, time1, time2):
        if time1 <= time2:
            return self >= time1 and self < time2
        else:
            return self >= time2 and self < time1
