import sqlite3

mycurs = sqlite3.connect('my_11.db')  
curs = mycurs.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS match (player TEXT NOT NULL,scored INTEGER,faced INTEGER,fours INTEGER,sixes INTEGER,bowled INTEGER,maiden INTEGER,given INTEGER,wkts INTEGER,catches INTEGER,stumping INTEGER,ro INTEGER);''')



curs.execute('''CREATE TABLE IF NOT EXISTS stats (player PRIMARY KEY,matches INTEGER,runs INTEGER,hundreds INTEGER,fifties INTEGER,value INTEGER,ctg TEXT NOT NULL);''')


curs.execute('''CREATE TABLE IF NOT EXISTS teams (name TEXT NOT NULL,players TEXT NOT NULL,value INTEGER);''')



sql="select * from match"
curs.execute(sql)
result=curs.fetchall()
if(result):
    for i in result:
        
    
        print(i)
    opt=input("\n add more players details ? (Y/N) : ")
else:
    print("No data found ")

    opt=input("\n add players data (Y/N) :")
while(opt=='y' or opt=='Y'):
    
    row=[input("Player name :")]
    row.append(int(input("Runs Scored: ")))
    row.append(int(input("Balls Faced: ")))
    row.append(int(input("Fours: ")))
    row.append(int(input("Sixes: ")))
    row.append(int(input("Balls Bowled: ")))
    row.append(int(input("Maiden Overs: ")))
    row.append(int(input("Runs Given: ")))
    row.append(int(input("Wickets Taken: ")))
    row.append(int(input("Catches: ")))
    row.append(int(input("Stumping: ")))
    row.append(int(input("Run Outs: ")))
    
    
    try:
        curs.execute("INSERT INTO match (player,scored, faced, fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", 
                          (row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        mycurs.commit()

        print("records added successfully match table.")
    except:    
        print("Error in operation.")
        mycurs.rollback()
   

        
    print("player information for Stats table ")
    row.append(int(input("Total matches: ")))
    row.append(int(input("Total runs: ")))
    row.append(int(input("100s: ")))
    row.append(int(input("50s: ")))
    row.append(int(input("Value: ")))
    row.append(input("Category as (BAT,BWL,AR,WK): "))
    
    try:      
    
        curs.execute("INSERT INTO stats (player,matches,runs, hundreds, fifties,value,ctg) VALUES (?,?,?,?,?,?,?)", 
                          (row[0],row[12], row[13], row[14],row[15],row[16],row[17]))
        mycurs.commit()

        print("records added successfully for stats table.")
    except:    
        print("Error in operation.")
        mycurs.rollback()
        
    opt=input("adding more player ? (Y/N) : ")

   
        
        

        
print("bye")   
curs.close() 

    
    
    
    
    
    

    
    

    
    
    
    
    
 
                          
        

        
     
        
        
    
    
    
        

    
    
    
    
    

    
    
         
    
    
                          
        

    
    
        
        
        
    
    
        

    

