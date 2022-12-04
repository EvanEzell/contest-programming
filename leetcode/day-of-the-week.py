// https://leetcode.com/problems/day-of-the-week

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        def isLeapYear(year):
            if year % 4 == 0:
                if year % 100 == 0:
                    return year % 400 == 0
                else:
                    return True
            else:
                return False

        days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        days_in_month_normal = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        days_in_month_leap = [0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

        daysSinceEpoch = 0
        daysSinceEpoch += (year - 1971) * 365
        daysSinceEpoch += (year - 1 - 1971 + 3) // 4

        days_in_month = days_in_month_normal if not isLeapYear(year) else days_in_month_leap
        daysSinceEpoch += days_in_month[month]
        
        daysSinceEpoch += day
        
        return days[daysSinceEpoch % 7]
        