from datetime import date
import sys
class DateUtil:


        def check_no_of_days(self, date1, date2 ):
            # date1 = date(2014, 7, 2)
            # date2 = date(2014, 7, 11)
            try:
                delta = self.get_day_month_year(date1) - self.get_day_month_year(date2)
                print(delta.days)
                return (delta.days)
            except:
                print("""Date of birth is not in correct format. It should be "YYYY-mm-dd" """)

        def get_day_month_year(self, date_input):

                yy, mm, dd = str(date_input).split("-")
                return date(int(yy), int(mm), int(dd))

        def check_date_of_birth(self, dob):
            date_format = "%Y-%m-%d"
            try:
                yy, mm, dd = str(dob).split("-")

                dob_entered = date(int(yy), int(mm), int(dd))
                age = self.calculate_age(dob_entered)

                if age < 24:
                    print("Sorry !! Age should be more than 24 years.")
                    return False
                else:
                    return True
            except ValueError:
                print(sys.exc_info()[1])

            # dob_entered = datetime.datetime.strptime(dob, date_format)

        def calculate_age(self, dob):
            today = date.today()
            return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))



