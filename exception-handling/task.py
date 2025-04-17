class InsufficientBalanceerror(BaseException):
    def __init__(self,msg):
        self.msg = msg
class InvalidPinerror(BaseException):
    def __init__(self,msg):
        self.msg = msg
class Bank:
    bankname='sbi'
    bankbranch='delhi'
    bankintrest=7
    def __init__(self, cname, caccount, cmobile,cpin,cbalance):
        self.cname=cname
        self.caccount=caccount
        self.cmobile=cmobile
        self.cpin=cpin
        self.cbalance=cbalance
    def withdrawl(self):
        try:
            pinn=int(input('enter the pin:-'))
            if pinn==self.cpin:
                amount=int(input('enter the amount:-'))
                if amount<=self.cbalance:
                    self.cbalance=self.cbalance-amount
                    print('amount successfully withdrawled')
                else:
                    raise InsufficientBalanceerror ('u have less balance')
            else:
                raise InvalidPinerror ('invalid pin')
        except InsufficientBalanceerror as ibe:
            print(ibe)
        except InvalidPinerror as ipe:
            print(ipe)
        print('remaing gets executed as it is')
ad=Bank('charan',103020,8989898989,1234,20000)
ad.withdrawl()
            
            
                    