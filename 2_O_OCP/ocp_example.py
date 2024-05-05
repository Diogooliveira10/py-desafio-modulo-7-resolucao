class Programmer:
    def make(self):
        print("Programmer creating code")

class Seller:
    def make(self):
        print("Seller selling the product")

class HR:
    def make(self):
        print("HR hiring new devs")

class Company:
    def do_work(self, worker: any) -> None:
        # lógica antes do make
        worker.make()

programmer = Programmer()
seller = Seller()
hr = HR()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(hr)
