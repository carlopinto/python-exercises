class BespokeMethods:
    
    def absolute_value(n):
        if n >= 0:
            return n
        else:
            return -n

    def turn_clockwise(p):
        points = ["N", "E", "S", "W"]
        if p in points:
            index = points.index(p)
            if index == 3:
                return points[0]
            else:
                return points[index + 1]
        else:
            return None

    def day_name(i):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        if i >= 0 and i <= 6:
            return days[i]
        else:
            return None

    def day_num(day):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        if day in days:
            return days.index(day)
        else:
            None

    def day_add(day, delta):
        increment = delta % 7
        day_back = (BespokeMethods.day_num(day) + increment) % 7
        return BespokeMethods.day_name(day_back)

    def month_num(month):
        months =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        if month in months:
            return months.index(month)
        else:
            None

    def days_in_month(m):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if BespokeMethods.month_num(m) != None:
            return days[BespokeMethods.month_num(m)]
        else:
            None
        return

    def to_secs(h, m, s):
        h_to_s = h * 3600
        m_to_s = m * 60
        return int(s + h_to_s + m_to_s)

    def hours_in(s):
        return s // 3600

    def minutes_in(s):
        return (s - BespokeMethods.hours_in(s) * 3600) // 60

    def seconds_in(s):
        if s < 0:
            return None
        a = BespokeMethods.hours_in(s) * 3600
        b =  BespokeMethods.minutes_in(s) * 60
        return s - a - b

    def compare(a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

    def hypotenuse(s1, s2):
            return (s1 ** 2 + s2 ** 2) ** 0.5

    def slope(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    def intercept(x1, y1, x2, y2):
        return y1 - BespokeMethods.slope(x1, y1, x2, y2) * x1

    def is_even(n):
        if type(n) == int:
            return n % 2 == 0
        else:
            return None

    def is_odd(n):
        if BespokeMethods.is_even(n) is None:
            return None
        else:
            return not BespokeMethods.is_even(n)  

    def is_factor(f, n):
        return n % f == 0

    def is_multiple(n1, n2):
        return BespokeMethods.is_factor(n2, n1)

    def f2c(f):
        return round((f-32)*5/9)

    def c2f(c):
        return round(c*9/5 + 32)
    
    def sum_list_elements(list):
        total = 0
        for e in list:
            total = total + e
        
        return total
