from app_database import Database

class Model(Database):
    def __init__(self):
        """
            Create connection to database for application.
        """
        Database.__init__(self)

        """
            Create Tables for application.
            1. field_staff_information
            2. participant_log
        """
            #Field Staff TABLE
        self.pointer.execute("CREATE TABLE IF NOT EXISTS field_staff_information (id INTEGER PRIMARY KEY, staff text UNIQUE)")
            #Participant Log TABLE
        self.pointer.execute("CREATE TABLE IF NOT EXISTS participant_log (id INTEGER PRIMARY KEY, date_ent date, part_ffq_id text UNIQUE, part_24_id text, part_names text, part_sex text, part_tribe text, part_age text, part_pnum1 text, part_pnum2 text, part_ses text)")
        self.connection.commit()

############ SENDER INFORMATION TABLE
    def insert_field_staff_information(self, a):
        self.pointer.execute("INSERT INTO field_staff_information VALUES (NULL,?)",(a,))
        self.connection.commit()

    def view_field_staff_information(self):
        self.pointer.execute("SELECT * FROM field_staff_information")
        rows = self.pointer.fetchall()
        return rows

############ CERTIFICATE RECORDS
    def insert_participant_log(self, a, b, c, d, e, f, g, h, i, j):
        self.pointer.execute("INSERT INTO participant_log VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i,j,))
        self.connection.commit()

    def view_participant_log(self):
        self.pointer.execute("SELECT * FROM participant_log ORDER BY part_ffq_id")
        rows = self.pointer.fetchall()
        return rows

    def view_participant_log_by_id(self, a):
        self.pointer.execute("SELECT * FROM participant_log WHERE part_ffq_id =?",(a,))
        rows = self.pointer.fetchall()
        return rows

    def update_participant_log(self, i, a, b, c, d, e, f, g, h):
        self.pointer.execute("UPDATE participant_log SET  date_ent=?, part_names=?, part_sex=?, part_tribe=?, part_age=?, part_pnum1=?, part_pnum2=?, part_ses=? WHERE part_ffq_id=?",(a,b,c,d,e,f,g,h,i))
        self.connection.commit()

    def update_participant_log_x(self, c, a, b):
        self.pointer.execute("UPDATE participant_log SET part_ffq_id=?, part_24_id=? WHERE part_pnum1=?",(a,b,c))
        self.connection.commit()
