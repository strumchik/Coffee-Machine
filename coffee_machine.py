class CoffeeMachine:
    needs = {"water": (250, 350, 200), "coffee beans": (16, 20, 12), "milk": (0, 75, 100),
             "disposable cups": (1, 1, 1), "money": (-4, -7, -6)}
    supply = {"water": 400, "milk": 540, "coffee beans": 120, "disposable cups": 9, "money": 550}

    def coffee(self, a):
        if a == "back":
            return
        else:
            b = int(a) - 1
            not_enough = []
            for key in self.needs.keys():
                if self.supply[key] < self.needs[key][b]:
                    not_enough.append(str(key))
            if not_enough:
                print("Sorry, not enough " + ', '.join(not_enough), "!\n")
            else:
                for key in self.needs.keys():
                    self.supply[key] -= self.needs[key][b]
                print("I have enough resources, making you a coffee!\n")

    def menu(self):
        while True:
            act = (input("Write action (buy, fill, take, remaining, exit):\n"))
            if act == "buy":
                self.coffee(input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                  "menu:\n"))
            elif act == "fill":
                self.supply["water"] += int(input("Write how many ml of water do you want to add:\n"))
                self.supply["milk"] += int(input("Write how many ml of milk do you want to add:\n"))
                self.supply["coffee beans"] += int(input("Write how many grams of coffee beans do you want to add:\n"))
                self.supply["disposable cups"] += int(
                    input("Write how many disposable cups of coffee do you want to add:\n"))
            elif act == "take":
                print(f"I gave you ${self.supply['money']}")
                self.supply['money'] = 0
            elif act == "remaining":
                print(f"The coffee machine has:\n")
                for key in self.supply.keys():
                    print(f"{self.supply[key]} of {str(key)}")
            elif act == "exit":
                break


cm = CoffeeMachine()
cm.menu()
