import mysql.connector

class sql_handler():

    def __init__(self):
        self.db = mysql.connector.connect(
            host = "",
            user = "",
            passwd = "",
            database = ""
        )
        
        self.cursor = self.db.cursor()

    def insert (self , table :str , columns:str , values : tuple):
        string = ""
        for x in columns:
            string = string + x +","
        
        print ("""INSERT INTO {} ({}) VALUES {}""".format(table,string[:-1],values))
        self.cursor.execute("""INSERT INTO {} ({}) VALUES {}""".format(table,string[:-1],values))
        self.db.commit()

    def get_collumn (self, table :str , column : str):
        self.cursor.execute("SELECT {} FROM {}".format(column,table))
        
        return self.cursor.fetchall()
    
    def get_collumn(self,table:str ,columns:str ,where:str):
        print ("""SELECT {} FROM {} WHERE ({})""".format(columns,table,where))
        self.cursor.execute("""SELECT {} FROM {} WHERE ({})""".format(columns,table,where))
        
        return self.cursor.fetchall()
    
    def add_money(self,serverID,memberID,amount):
        money = self.get_collumn("Member","Balaceni","ServerID ={} AND UserID ={}".format(serverID,memberID))
        money[0] = round(float(str(money[0])[1:-2]) + amount,2)

        self.cursor.execute("UPDATE Member SET Balaceni={} WHERE ServerID={} AND UserID={}".format(money[0],serverID,memberID))
        self.db.commit()

    def get_money(self,serverID,memberID):
        output = self.get_collumn("Member","Balaceni","ServerID ={} AND UserID ={}".format(serverID,memberID))
        
        return float(str(output[0])[1:-2])

    def remove_money(self,serverID,memberID,amount):
        succes= True

        print (amount ,self.get_money(serverID , memberID))

        if amount <= self.get_money(serverID , memberID):
            money = self.get_money(serverID,memberID)
            money = money-amount

            self.cursor.execute("UPDATE Member SET Balaceni={} WHERE ServerID={} AND UserID={}".format(money,serverID,memberID))
            self.db.commit()
        else:
            print("I got here somehow")
            succes = False
        
        return succes

    def commitdb (self):
        self.db.commit()