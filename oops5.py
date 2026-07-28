class login:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self,username,password):
        if username==self.username and password==self.password:
              print("login successfully")
              return True
        else:
             print("invalid username or password")
             return False
class OTPVerification:
    def __init__(self):
        self.otp = 1234
    def verify_otp(self, user_otp):
        if user_otp == self.otp:
            print("OTP Verified Successfully")
            return True
        else:
            print("Invalid OTP")
            return False
class SecureBank(login,OTPVerification):
    def __init__(self, username,password):
        login.__init__(self, username, password)
        OTPVerification.__init__(self)
        self.balance = 10000 
    def dashboard(self):
        print("\n----- DASHBOARD -----")
        print("Balance:", self.balance)
        print("Minimum Balance:1000")
        print("Mini Statement:")
        print("1. Deposit:+5000")
        print("2. Withdrawal:-2000")
        print("Money Transfer:Available")
        print("Logout Successful")
username = input("Enter Username: ")
password = input("Enter Password: ")
bank = SecureBank("admin", "1234")
if bank.login(username, password):
    otp = int(input("Enter OTP: "))
    if bank.verify_otp(otp):
        bank.dashboard()