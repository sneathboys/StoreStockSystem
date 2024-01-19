class Bike:
    def __init__(self, model, costToBuy, retailPrice):
        self.Model = model
        self.BuyPrice = costToBuy
        self.RetailPrice = retailPrice

    def infoAboutProduct(self):
        print("model is:", self.Model, "\n cost to buy:", self.BuyPrice, "\n what we sell for:", self.RetailPrice )


bike1 = Bike("Giant", "100", "200")
print(bike1.infoAboutProduct())
    

