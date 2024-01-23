import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk, Image


class shopStockManagment:

    def __init__(self,root):
        self.root = root
        self.root.geometry("800x600")
        self.employees = []
        self.suppliers = []
        self.productsWork = productsClass()
        self.salesWork = salesClass()
        self.categoryWork = categoryClass()
        self.mainGUI()

    def mainGUI(self):
        #top bar gui placment
        topFrame = tk.Frame(self.root, background="blue")
        topFrame.place(x=0,y=0, width=800, height=60)

        self.icon_title = tk.PhotoImage(file="ALevelCodingProject/shopping-cart-icon.png")
        self.icon_title = self.icon_title.subsample(45,45)
        iconImag = tk.Label(topFrame, image= self.icon_title, bg = "blue")
        iconImag.grid(row=0, column=1)
        welcomeText = tk.Label(topFrame, fg="white", text="Inventory managment system", bg="blue",font="Arial, 30")
        welcomeText.grid(row=0, column=3)


        #side bar gui placment
        sideBarFrame = tk.Frame(self.root, background="grey")
        sideBarFrame.place(x=0, y=60, height=740, width=200)

        self.side_icon = tk.PhotoImage(file="ALevelCodingProject/last.png")
        self.side_icon = self.side_icon.subsample(7,7)
        sideImage = tk.Label(sideBarFrame, image=self.side_icon, background="grey")
        sideImage.grid(row=0,column=0)
        
        #menu tag for sidebar 
        menuLabel = tk.Label(sideBarFrame, text="Menu", font="Arial, 15", padx=73, background="cyan")
        menuLabel.grid(row=1, column=0)

        #buttons for side bar
        funcEmployeeButton = lambda:self.employeeButtonFunction()
        employeeButton = tk.Button(sideBarFrame, text="Employee", font="Arial, 12", padx=59, pady=10, command=funcEmployeeButton)
        employeeButton.grid(row=2,column=0)

        funcSuplierButton = lambda:self.supplierButtonFunction()
        supplierButton = tk.Button(sideBarFrame, text="Supplier", font="Arial, 12", padx=65, pady=10, command=funcSuplierButton)
        supplierButton.grid(row=3, column=0)

        categoryButton = tk.Button(sideBarFrame, text="Category",font="Arial, 12", padx=62, pady=10, command=self.categoryWork.displayGUI)
        categoryButton.grid(row=4, column=0)

        funcProductsButton = lambda:self.productsButtonFunction()
        productsButton = tk.Button(sideBarFrame, text="Products", font="Arial, 12", padx=63, pady=10, command=funcProductsButton)
        productsButton.grid(row=5, column=0)

        salesButtonFunc = lambda:self.salesButtonFunction()
        salesButton = tk.Button(sideBarFrame, text = "Sales", font="Arial, 12", padx=74, pady=10, command=salesButtonFunc)
        salesButton.grid(row=6, column=0)

        exitButton = tk.Button(sideBarFrame, text="Exit", bg="red", font="Arial, 20", padx=68, pady=28)
        exitButton.grid(row=7, column=0)

        returnedprofits =lambda: self.salesWork.returnProfits()
        def prof():
            profitLable = tk.Label(self.root, background="yellow", text = 'Total Profits: \n £'+ str(returnedprofits()), font="Arial, 14",borderwidth=10, relief="ridge")
            profitLable.place(x = 250, y = 110, width=150, height=150)
            self.root.after(1000, prof)
        prof()

    
    def employeeButtonFunction(self):
        empolyeeView = tk.Toplevel()

        empolyeeView.geometry("800x600")

        #Introduction to employee view
        titleFrame = tk.Frame(empolyeeView, background="blue")
        titleFrame.place(x=0, y=0, width=800, height= 80)
        self.titleFrameImage = tk.PhotoImage(file="ALevelCodingProject/job.png")
        self.titleFrameImage = self.titleFrameImage.subsample(15,15)
        displayTitleFrameImage = tk.Label(titleFrame, image=self.titleFrameImage, background="blue")
        displayTitleFrameImage.grid(row=0, column=0)
        textTitleFrame = tk.Label(titleFrame, text="Employee Stats Search:", fg="white", bg="blue",font="Arial, 30")
        textTitleFrame.grid(row=0, column=4)

        #input field for employee information

        inputFeildFrame = tk.Frame(empolyeeView)
        inputFeildFrame.place(x=0, y= 80, width=800, height=150)

        employeeNameLabel = tk.Label(inputFeildFrame, text="Enter Employee Name:", font="Arial, 15", bg ="grey")
        employeeNameLabel.grid(row=0, column=0)

        employeeNameEntry = tk.Entry(inputFeildFrame, width=15, font="Arial, 14")
        employeeNameEntry.grid(row=0, column=1)

        employeeIDLabel = tk.Label(inputFeildFrame, text="Employee ID:", font="Arial, 14", bg= "grey")
        employeeIDLabel.grid(row=0, column = 3)
        
        employeeIDEntry = tk.Entry(inputFeildFrame, width=15, font="Arial, 14")
        employeeIDEntry.grid(row=0, column=4)

        gap = tk.Label(inputFeildFrame, padx=50, pady=10)
        gap.grid(row=0,column=2)

        enterEmployeeNameButton = tk.Button(inputFeildFrame, text="Search Employee Name", font="Arial, 12",bg="grey")
        enterEmployeeNameButton.grid(column=0, row=1)

        enterEmployeeIDButton = tk.Button(inputFeildFrame, text="Search Employee ID", font="Arial, 12", bg="grey")
        enterEmployeeIDButton.grid(row=1, column=3)



        returnFrame = tk.Frame(empolyeeView)
        returnFrame.place(x=0, y=150, width=800, height= 100)

        blank = tk.Label(returnFrame)
        blank.grid(row=2, column=0)


        returnedDataNameLabel = tk.Label(returnFrame, text="Returned Name:", font="Arial, 8")
        returnedDataNameLabel.grid(row=3, column=0)
        returnedDataNameEntry = tk.Entry(returnFrame, font="Arial, 8")
        returnedDataNameEntry.grid(column=1, row=3)

        returnedDataIDLabel = tk.Label(returnFrame, text="Returned Employee ID:", font="Arial, 8")
        returnedDataIDLabel.grid(row = 3, column = 3)
        returnedDataIDEntry = tk.Entry(returnFrame, font="Arial, 8")
        returnedDataIDEntry.grid(row = 3, column = 4)

        returnedDataSalesFiguresLabel = tk.Label(returnFrame, text = "Sales Data of Employee:", font="Arial, 8")
        returnedDataSalesFiguresLabel.grid(row=3, column=5)
        returnedDataSalesFiguresEntry = tk.Entry(returnFrame, font="Arial, 8")
        returnedDataSalesFiguresEntry.grid(row=3, column=6)

        empolyeeView.mainloop()
    
    def supplierButtonFunction(self):
        supGUI = tk.Toplevel()

        supGUI.geometry("800x600")

        titleSupFrame = tk.Frame(supGUI, background="grey")
        titleSupFrame.place(x=0, y=0, height=80, width=800)

        self.supplierImage = tk.PhotoImage(file="ALevelCodingProject/supplier.png")
        self.supplierImage = self.supplierImage.subsample(7,7)
        supplierImageLabel = tk.Label(titleSupFrame, image=self.supplierImage, background="grey")
        supplierImageLabel.grid(column=0, row=0)

        space= tk.Label(titleSupFrame,padx=40, background="grey")
        space.grid(row=0, column=1)


        titleText = tk.Label(titleSupFrame, text="Supplier Add, View Or delete", font="Arial, 25", background="grey")
        titleText.grid(row=0,column=2)

        InputFeildSupplierFrame = tk.Frame(supGUI)
        InputFeildSupplierFrame.place(x=0, y=80, height=150, width=800)

        supplierNameLabel = tk.Label(InputFeildSupplierFrame, text= "Name Of Supplier:", font="Arial, 12")
        supplierNameLabel.grid(row=0, column=0)

        supplierNameEntry = tk.Entry(InputFeildSupplierFrame, font="Arial, 12")
        supplierNameEntry.grid(row=0, column=1)

        supplierProductLabel = tk.Label(InputFeildSupplierFrame,text="Products supplied seperated by a semi-colon:", font="Arial, 12")
        supplierProductLabel.grid(row=0, column=2)

        supplierProductEntry = tk.Entry(InputFeildSupplierFrame, font = "Arial, 12")
        supplierProductEntry.grid(row=0, column=3)

        b = tk.Label(InputFeildSupplierFrame)
        b.grid(row=1, column=0, pady=10)

        supplierButtonFunc = lambda:self.actionEnterSupplier(supplierNameEntry, supplierProductEntry, TableProducts)
        enterSupplierInfoButton = tk.Button(InputFeildSupplierFrame, font="Arial, 12", text="Enter", command=supplierButtonFunc)
        enterSupplierInfoButton.grid(row=2, column=1, columnspan=2)

        TableProducts = ttk.Treeview(supGUI, columns=("Supplier", "Products"), show="headings")
        TableProducts.heading("Supplier", text= "Supplier Name")
        TableProducts.heading("Products", text = "Products")

        TableProducts.place(x=0, y=230, width=800, height=370)

        suppliersLength = len(self.suppliers)
        SUPinfo = self.suppliers        


        TableProducts.delete(*TableProducts.get_children())
        
        for NameOfSupplier in range(0, suppliersLength):
            nameDictonary= SUPinfo[NameOfSupplier]
            finalName = nameDictonary["Name"]

            prod = nameDictonary["Product"]

            finalProd = prod.split(';')

            TableProducts.insert(parent = '', index =NameOfSupplier, values = (finalName, finalProd))




        supGUI.mainloop()

    def actionEnterSupplier(self, supplierNameEntry, supplierProductEntry, TableProducts):
        supplierName = supplierNameEntry.get()
        supplierProduct = supplierProductEntry.get()


        supplierInfo = {
            "Name": supplierName,
            "Product": supplierProduct
        }
        
        self.suppliers.append(supplierInfo)

        suppliersLength = len(self.suppliers)
        SUPinfo = self.suppliers        


        TableProducts.delete(*TableProducts.get_children())
        
        for NameOfSupplier in range(0, suppliersLength):
            nameDictonary= SUPinfo[NameOfSupplier]
            finalName = nameDictonary["Name"]

            prod = nameDictonary["Product"]

            finalProd = prod.split(';')

            TableProducts.insert(parent = '', index =NameOfSupplier, values = (finalName, finalProd))
    
    def productsButtonFunction(self):
        productPage = tk.Toplevel()

        productPage.geometry("800x600")

        productPageTitleFrame = tk.Frame(productPage, background="blue")
        productPageTitleFrame.place(x=0, y=0, width=800, height=80)

        self.productPageTitleImage = tk.PhotoImage(file="ALevelCodingProject/product-png-9.png")
        self.productPageTitleImage = self.productPageTitleImage.subsample(7,7)
        displayProductPageTitleImage = tk.Label(productPage, image=self.productPageTitleImage, background="blue")
        displayProductPageTitleImage.grid(row=0, column =0)

        bl = tk.Label(productPageTitleFrame, background="blue", padx = 150)
        bl.grid(row = 0, column=1) 
        
        productPageTitleLabel = tk.Label(productPageTitleFrame, text="Product View", font="Arial, 25", background="blue")
        productPageTitleLabel.grid(row=0 ,column=2)

        productPageCollectFrame = tk.Frame(productPage)
        productPageCollectFrame.place(x=0, y=80, width = 800, height = 200)

        productNameLabel = tk.Label(productPageCollectFrame, text="Product Name:", font="Arial, 12")
        productNameLabel.grid(row=0, column=0)
        productNameEntry = tk.Entry(productPageCollectFrame, font="Arial, 12")
        productNameEntry.grid(row=0, column=1)
        
        blank1 = tk.Label(productPageCollectFrame, padx=60)
        blank1.grid(row=0, column=2)

        productRRPLabel = tk.Label(productPageCollectFrame, text="Product RRP:", font="Arial, 12")
        productRRPLabel.grid(row=0, column=3)
        productRRPEntry = tk.Entry(productPageCollectFrame, font="Arial, 12")
        productRRPEntry.grid(row= 0, column=4)

        productCostLabel = tk.Label(productPageCollectFrame, text="Product Cost:", font="Arial, 12")
        productCostLabel.grid(row=1, column=0)
        productsCostEntry = tk.Entry(productPageCollectFrame, font="Arial, 12")
        productsCostEntry.grid(row=1, column=1)

        blank2 = tk.Label(productPageCollectFrame, padx=60)
        blank2.grid(row=1, column=2)

        productQuantityLabel = tk.Label(productPageCollectFrame, text="Product Quantity:", font="Arial, 12")
        productQuantityLabel.grid(row=1, column=3)
        productQuantityEntry = tk.Entry(productPageCollectFrame, font="Arial, 12")
        productQuantityEntry.grid(row=1, column=4)



        productTable = ttk.Treeview(productPage, columns=("Product ID", "Product Name", "Product RRP", "Product Cost", "Product Quantity"), show="headings")
        productTable.heading("Product ID", text="Product ID")
        productTable.heading("Product RRP", text="Product RRP")
        productTable.heading("Product Name", text = "Product Name")
        productTable.heading("Product Cost", text="Product Cost")
        productTable.heading("Product Quantity", text="product Quantity")

        productTable.place(x = 0, y = 180, height=320, width=780)

        self.productsWork.updateTable(productTable)

        scrollBar = ttk.Scrollbar(productPage, orient="vertical", command=productTable.yview)
        scrollBar.place(x = 780, y =180, width=20, height = 320)
        productTable.configure(yscrollcommand=scrollBar.set)
        scrollBarHorizontle = ttk.Scrollbar(productPage, orient="horizontal", command=productTable.xview)
        scrollBarHorizontle.place(x=0, y= 500, width=800, height=20)
        productTable.configure(xscrollcommand=scrollBarHorizontle.set)

        submitButtonProductFunc = lambda: self.productsWork.newProduct(productNameEntry.get(), productRRPEntry.get(), productsCostEntry.get(), productQuantityEntry.get(), productTable)
        submitButtonProduct = tk.Button(productPageCollectFrame, text="Submit Product", font="Arial, 12", command=submitButtonProductFunc)
        submitButtonProduct.grid(row = 2, column=2)

        productPage.mainloop()

    def salesButtonFunction(self):
        salesPage = tk.Toplevel()

        salesPage.geometry("800x600")

        titleSalesFrame = tk.Frame(salesPage, background="blue")
        titleSalesFrame.place(x=0, y=0, width=800, height=80)

        self.salesImage = tk.PhotoImage(file="ALevelCodingProject/sales-icon-15.png")
        self.salesImage = self.salesImage.subsample(7,7)
        salesImageLable = tk.Label(titleSalesFrame, image=self.salesImage, background="blue")
        salesImageLable.grid(row=0, column=0)

        blankSpace = tk.Label(titleSalesFrame, padx=125, background="blue")
        blankSpace.grid(row=0, column=1)

        titleSalesTextLable = tk.Label(titleSalesFrame, text="Sales Page", font="Arial, 25", background="blue", foreground="white")
        titleSalesTextLable.grid(row=0, column=2)

        soldItemFrame = tk.Frame(salesPage)
        soldItemFrame.place(x=0, y = 80, height = 300, width=800)

        soldItemIDLable = tk.Label(soldItemFrame, text = "ID of Item Sold:", font="Arial, 14")
        soldItemIDLable.grid(row=0,column=0)
        soldItemIDEntry = tk.Entry(soldItemFrame, font="Arial, 14")
        soldItemIDEntry.grid(row=0, column=1)

        blankSpace2 = tk.Label(soldItemFrame, padx=5)
        blankSpace2.grid(row=0, column=2)

        soldItemQuantityLabel = tk.Label(soldItemFrame, font="Arial, 14",text = "Quantity of Item Sold:")
        soldItemQuantityLabel.grid(row= 0, column=3)
        soldItemQuantityEntry = tk.Entry(soldItemFrame, font="Arial, 14")
        soldItemQuantityEntry.grid(row=0, column=4)

        submitSoldItemButtonFunc = lambda: self.salesWork.itemSold(self.productsWork, soldItemIDEntry, soldItemQuantityEntry)
        submitSoldItemButton = tk.Button(soldItemFrame, text="Submit", font="Arial, 14", command=submitSoldItemButtonFunc)
        submitSoldItemButton.grid(row= 1, column=1, columnspan=3)


        salesPage.mainloop()

class categoryClass:
    def __init__(self):
        return
    def displayGUI(self):
        categoryScreen = tk.Toplevel()
        categoryScreen.geometry("800x600")

        categoryTitleFrame = tk.Frame(categoryScreen, background="blue")
        categoryTitleFrame.place(x=0, y=0, width=800, height=80)

        self.categoryTitleImage = tk.PhotoImage(file = 'ALevelCodingProject/Category Image.png')
        imageDisplayLable = tk.Label(categoryTitleFrame, background="blue", image=self.categoryTitleImage)
        imageDisplayLable.grid(row=0,column=0)

        blank = tk.Lable = (categoryTitleFrame, background = 'blue', padx = 40)
        blank.grid(row=0, column =1)

        titleCategory  = tk.Lable(categoryTitleFrame, background = 'blue', text = 'Category Page', font = "Arial, 25")
        titleCategory.grid(row = 0, column =2)

        categoryScreen.mainloop()


class productsClass:
    def __init__(self):
        self.productsInfo = []
    
    def newProduct(self, prodName, prodRRP, prodCost, prodQuantity, productTable):
        if len(prodName) > 0:
            ID = len(self.productsInfo)
            self.productsInfo.append({
                "name": prodName,
                "RRP": prodRRP,
                "cost": prodCost,
                "quantity": prodQuantity,
                "ID": ID
            })

            productTable = self.updateTable(productTable)
            return productTable

    def updateQuantity(self, prodID, changeAmount):
        for productInfoRange in range (0, len(self.productsInfo)):
            dictonaryies = self.productsInfo[productInfoRange]
            searchID = dictonaryies["ID"]
            
            if searchID == prodID:
                dictonaryies["quantity"] = changeAmount
        
    
    def removeProduct(self, prodID):
        for productInfoRange in range (0, len(self.productsInfo)):
            dictonaryies = self.productsInfo[productInfoRange]
            searchID = dictonaryies["ID"]
            
            if searchID == prodID:
                dictonaryies["name"] = "Deleted"
                dictonaryies["ID"] = "Deleted"

    def updateTable(self, productTable):
        productTable.delete(*productTable.get_children())
        for x in range(0,len(self.productsInfo)):
            temp = self.productsInfo[x]
            IDCheck = temp["ID"]
            if IDCheck != "Deleted":
                name = temp["name"]
                rrp = temp["RRP"]
                cost = temp["cost"]
                quantity = temp["quantity"]
                productTable.insert(parent = '', index =x, values = (IDCheck, name, rrp, cost, quantity))
        
        return productTable
    
    def returnInfo(self):
        return self.productsInfo
    
    def updateDict(self, newDict):
        self.productsInfo = newDict

                
class salesClass:
    def __init__(self):
        self.profit = 0.00
        

    def itemSold(self, productsWork, soldItemIDEntry, soldItemQuantityEntry):
        productsDictArray = productsWork.returnInfo()
        validation = False
        for x in range(0, len(productsDictArray)):
            check = productsDictArray[x]
            if str(check["ID"]) == str(soldItemIDEntry.get()):
                try:
                    productsDictArray[x]["quantity"] = int(check["quantity"])- int(soldItemQuantityEntry.get())
                    validation = True
                except:
                    print("error")
        if validation == True:
            productsWork.updateDict(productsDictArray)
            self.profitCalc(productsWork, soldItemIDEntry, soldItemQuantityEntry) 
            validation = False


    def profitCalc(self, productsWork, soldItemIDEntry, soldItemQuantityEntry):
        listOfItems = productsWork.returnInfo()
        itemID = soldItemIDEntry.get()
        totalProfit = 0
        for x in range(0, len(listOfItems)):
            currentDictionary = listOfItems[x]
            print(currentDictionary)
            print(type(itemID), type(currentDictionary["ID"]))
            if float(itemID) == float(currentDictionary["ID"]):
                getRRP = currentDictionary["RRP"]
                getCost = currentDictionary["cost"]
                print(getCost)
                try:
                    getRRP = float(getRRP)
                    getCost=float(getCost)
                except:
                    print("Error Not Number")
                
                try:
                    multiplier = soldItemQuantityEntry.get()
                    multiplier = float(multiplier)
                    getRRP = getRRP * multiplier
                    getCost = getCost * multiplier
                    totalProfit = getRRP - getCost
                except:
                    print("Error")
                
        self.profit = self.profit + totalProfit

        


    def returnProfits(self):
        temp = self.profit
        return temp








if __name__ == "__main__":
    root = tk.Tk()
    app = shopStockManagment(root)
    root.mainloop()
