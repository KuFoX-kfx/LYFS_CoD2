import sqlite3

class DB_api:
    
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        
    def DB_AddServer(self, IPandPORT, Name):
        with self.connection:
            return self.cursor.execute("INSERT INTO `servers` (`IPandPORT`,`Name`) VALUES(?,?)", (IPandPORT,Name))
        
    def DB_DelServer(self, Name):
        with self.connection:
            self.cursor.execute("delete from servers where Name = ?", (Name,))
            
    def DB_GetServers(self):
        with self.connection:
            self.cursor.execute("""SELECT Name from servers""")
            records = self.cursor.fetchall()
            #log.write("Всего строк:  ", len(records))
            temp = []
            for row in records:
                temp.append(row[0])
            return temp
    
    def DB_GetIP(self, Name):
        with self.connection:
            self.cursor.execute("select IPandPORT from servers where Name = ?", (Name,))
            return self.cursor.fetchone()
    
        
        
    def DB_PTG(self, PTG):
        with self.connection:
            self.cursor.execute("delete from PTG")
            return self.cursor.execute("INSERT INTO `PTG` (`PatchToGame`) VALUES(?)", (PTG,))
        
    def DB_GetPTG(self):
        with self.connection:
            self.cursor.execute("SELECT PatchToGame from PTG")
            return self.cursor.fetchone()
            


    def DB_SFC(self, SFC):
        with self.connection:
            self.cursor.execute("delete from SFC")
            return self.cursor.execute("INSERT INTO `SFC` (`SiteForCheck`) VALUES(?)", (SFC,))
        
    def DB_GetSFC(self):
        with self.connection:
            self.cursor.execute("SELECT SiteForCheck from SFC")
            return self.cursor.fetchone()

        
        
    def DB_close(self):
        self.connection.close()