import sqlite3


class Database:

    def __init__(self):
        self.con = sqlite3.connect('HRQnA.db')
        self.cursorObj = self.con.cursor()

    def create_table(self):
        self.cursorObj.execute("CREATE TABLE IF NOT EXISTS QnA(id integer PRIMARY KEY AUTOINCREMENT, Question text, Comments text)")
        self.con.commit()

    def insert_in_table(self,question,comment):
        self.cursorObj.execute("Insert into QnA(Question,Comments) VALUES(?,?)",(question,comment))
        self.con.commit()

    def fetch_hr_questions(self):
        self.cursorObj.execute("SELECT Question from QnA;")
        return self.cursorObj.fetchall()

    def fetch_comments(self):
        self.cursorObj.execute("SELECT comments from QnA;")
        return self.cursorObj.fetchall()

    def view_records(self):
        self.cursorObj.execute("Select * from QnA;")
        rows = self.cursorObj.fetchall()
        for row in rows:
            print(row)


if __name__ == '__main__':
    dbObj = Database()
    # dbObj.create_table()
    # dbObj.insert_in_table("Tell me something about yourself in brief","Ok. Glad to hear it !!")
    # dbObj.insert_in_table("Describe who you are? or Tell me about your background.","Ok. Nice !!")
    # dbObj.insert_in_table("What are your strengths and weaknesses?","How would you overcome your weaknesses ?")
    # dbObj.insert_in_table("You have not done your PG yet. This is not a drawback, but don’t you think you should get a PG degree asap?","Okay")
    # dbObj.insert_in_table("You have changed jobs/jumped ship too many times already, why so?","Okay.")
    # dbObj.insert_in_table("What are your strong points? or What are your strengths?","Very Impressive.")
    # dbObj.insert_in_table("What is your greatest fear?","Okay")
    # dbObj.insert_in_table("Do you have any serious medical issues?","Ok no worries.")
    # dbObj.insert_in_table("Did you ever have a conflict with your current/previous boss or professor?","Okay")
    # dbObj.insert_in_table("What do your friends/co-workers say about you?","Nice.")
    dbObj.view_records()


