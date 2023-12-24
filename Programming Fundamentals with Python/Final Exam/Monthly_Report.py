class Bakery:
    def __init__(self):
        self.distributors = {}
        self.clients = {}

    def deliver(self, distributor_name, money_spent):
        if distributor_name not in self.distributors:
            self.distributors[distributor_name] = 0
        self.distributors[distributor_name] += money_spent

    def return_money(self, distributor_name, money_returned):
        if distributor_name in self.distributors:
            if self.distributors[distributor_name] >= money_returned:
                self.distributors[distributor_name] -= money_returned
                if self.distributors[distributor_name] == 0:
                    del self.distributors[distributor_name]

    def sell(self, client_name, money_earned):
        if client_name not in self.clients:
            self.clients[client_name] = 0
        self.clients[client_name] += money_earned

    def print_info(self):
        for client, money_earned in self.clients.items():
            print(f"{client}: {money_earned:.2f}")
        print("-----------")
        for distributor, money_spent in self.distributors.items():
            print(f"{distributor}: {money_spent:.2f}")
        print("-----------")
        total_income = sum(self.clients.values())
        print(f"Total Income: {total_income:.2f}")


def main():
    bakery = Bakery()

    while True:
        command = input().split()
        if command[0] == "End":
            break
        elif command[0] == "Deliver":
            distributor_name, money_spent = command[1], float(command[2])
            bakery.deliver(distributor_name, money_spent)
        elif command[0] == "Return":
            distributor_name, money_returned = command[1], float(command[2])
            bakery.return_money(distributor_name, money_returned)
        elif command[0] == "Sell":
            client_name, money_earned = command[1], float(command[2])
            bakery.sell(client_name, money_earned)

    bakery.print_info()


# Example usage
main()
