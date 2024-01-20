import tkinter as tk
from tkinter import ttk


class BikeShopStockManagment:

    def __init__(self, root):
        self.root = root
        self.root.title("Shop Stock Managment System")
        self.stock = []
        self.profit = 0.0
        self.totalSold = 0
        self.GUI()
    
    def GUI(self):
        item = ttk.Label(self.root, text = "Item name: ")
        item.grid(row =0, column = 0)
        item_entry = ttk.Entry(self.root)
        item_entry.grid(row = 0, column=1)

        cost_label = ttk.Label(self.root, text = "Cost of Item: ")
        cost_label.grid(row = 1, column = 0)
        cost_entry = ttk.Entry(self.root)
        cost_entry.grid(row= 1, column= 1)

        rrp_label = ttk.Label(self.root, text="RRP:")
        rrp_label.grid(row = 2, column= 0)
        rrp_entry = ttk.Entry(self.root)
        rrp_entry.grid(row=2, column=1)

        quantity_label = ttk.Label(self.root, text="Quantity: ")
        quantity_label.grid(row = 3, column=0)
        quantity_entry = ttk.Entry(self.root)
        quantity_entry.grid(row=3, column=1)

        soldItem_label = ttk.Label(self.root, text = "Name of item sold: ")
        soldItem_label.grid(column=3, row=0)
        soldItem_entry = ttk.Entry(self.root)
        soldItem_entry.grid(column=4, row=0)

        quantitySold_label = ttk.Label(self.root, text = "Number Sold: ")
        quantitySold_label.grid(column=3,row=1)
        quantitySold_entry = ttk.Entry(self.root)
        quantitySold_entry.grid(column=4, row=1)


        w = lambda:self.viewStock()
        stockViewButton= ttk.Button(self.root, text="Click here to view stock", command = w)
        stockViewButton.grid(column=2, row=4)

        z = lambda: self.markSoldButtonCommand(soldItem_entry, quantitySold_entry, self.stock)
        markSold_button = ttk.Button(self.root, text= "Mark Sold", command=z)
        markSold_button.grid(column=3, row = 4, columnspan=2)



        x = lambda:self.InStock(quantity_entry, rrp_entry, cost_entry, item_entry)
        enter = ttk.Button(self.root, text="Enter Item: ", command= x)
        enter.grid(row=4, column=0, columnspan = 1)

        y = lambda:self.updateButtonCommand(quantity_entry, rrp_entry, cost_entry, item_entry)
        update = ttk.Button(self.root, text = "Update Item", command=y)
        update.grid(row=4, column = 1)


    def InStock(self, quantity_entry, rrp_entry, cost_entry, item_entry):
        stockItem = {
            "name": item_entry.get(),
            "cost": float(cost_entry.get()),
            "RRP": float(rrp_entry.get()),
            "quantity": int(quantity_entry.get())

        }
        self.stock.append(stockItem)
        item_entry.delete(0, tk.END)
        cost_entry.delete(0, tk.END)
        rrp_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)



        print(self.stock)
    
    def DisplayInsert(self, display):
        length = len(self.stock)
        previous = display.get()

        for itemInArray in range(0, length):
            temp = self.stock[itemInArray]
            name = temp["name"]
            cost = temp["cost"]
            rrp = temp["RRP"]
            quantity = temp["quantity"]

            compiled = "------------" + "\n name: " + str(name) + "\n Cost for you to buy: " + str(cost)+  "\n What you sell at: " + str(rrp) + "\n Quantity " + str(quantity)
            print(compiled)
            display.insert(0, str(previous) +"\n" + str(compiled))
            previous = display.get()

    def updateButtonCommand(self, quantity_entry, rrp_entry, cost_entry, item_entry):
        length = len(self.stock)
        item = item_entry.get()
        for x in range(0, length):
            temp = self.stock[x]
            nameOfItem = str(temp["name"])
            costOfItem = str(temp["cost"])
            rrpOfItem = str(temp["RRP"])
            quantityOfItem = str(temp["quantity"])
            print(nameOfItem)
            if nameOfItem == item:
                cost_entry.insert(0,costOfItem)
                rrp_entry.insert(0, rrpOfItem)
                quantity_entry.insert(0, quantityOfItem)
                self.stock.pop(x)

    def markSoldButtonCommand(self, soldItem_entry, quantitySold_entry,stock):
        length = len(self.stock)
        name = soldItem_entry.get()
        sold = quantitySold_entry.get()
        sold = float(sold)
        for arrayItteration in range(0,length):
            itemInfoFromArray = self.stock[arrayItteration]
            itemFromArray = itemInfoFromArray["name"]
            if itemFromArray == name:
                quanityFromArray = itemInfoFromArray["quantity"]
                rrpFromArray = itemInfoFromArray["RRP"]
                costFromArray = itemInfoFromArray["cost"]

                self.stock.pop(arrayItteration)
                quanityFromArray = quanityFromArray - sold

                temp = {
                    "name":itemFromArray,
                    "cost": costFromArray,
                    "RRP": rrpFromArray,
                    "quantity":quanityFromArray
                }
                self.stock.append(temp)
                print(self.stock)

    def viewStock(self):
        stockView = tk.Toplevel()
        stockView.title("Stock View")

        display = ttk.Treeview(stockView, columns=("Item","Cost","RRP","Quantity"), show="headings")
        display.heading("Item", text = "Item")
        display.heading("Cost", text = "Cost")
        display.heading("RRP", text = "RRP")
        display.heading("Quantity", text = "Quantity")
        display.grid(column= 2, row = 0)

        for i in range(0, len(self.stock)):
            dictionary = self.stock[i]
            Item1 = dictionary["name"]
            cost1 = dictionary["cost"]
            rrp1 = dictionary["RRP"]
            quantity1 = dictionary["quantity"]

            display.insert(parent='', index=i, values=(Item1, cost1, rrp1, quantity1))



                
            


if __name__ == "__main__":
    root = tk.Tk()
    app = BikeShopStockManagment(root)
    root.mainloop()