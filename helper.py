import mysql.connector as connector
class NotesDatabaseHelper:
    def __init__(self):
        self.connection=connector.connect(host='localhost',port='3306',user='root',password='******',database='databasename')
        query='create table if not exists notes(s_no int primary key,notes_name varchar(50),notes_subject varchar(20),notes_written_area varchar(200),notes_description varchar(30))'
        cur=self.connection.cursor()
        cur.execute(query)
        print('Created Notes Table Successfully...!!!');
    def createNote(self,serial_no,name,subject,content,description):
        query="insert into notes(s_no,notes_name,notes_subject,notes_written_area,notes_description) values({},'{}','{}','{}','{}')".format(serial_no,name,subject,content,description);
        cursor=self.connection.cursor();
        cursor.execute(query);
        self.connection.commit();
        # print('Note Created Successfully...!!')
    def showAllNotes(self):
        query="select * from notes"
        cursor=self.connection.cursor();
        cursor.execute(query);
        for x in cursor:
            print("---------------RECORD OF EACH NOTES-----------------")
            print("S/No. :",x[0]);
            print("NOTES NAME :",x[1]);
            print("NOTES SUBJECT :",x[2]);
            print("NOTES CONTENT :",x[3]);
            print("NOTES DESCRITION :",x[4]);
            print("--------------------------------------------------------------------------------")
    def updateNotes(self,s_no):
        upChoice=int(input("Which type of update you want? \n for 'name' press 1 \n for 'subject' press 2 \n for 'content' press 3 \n for 'description' press 4 "));
        cursor=self.connection.cursor();
     
        if upChoice == 1:
            notes_name=input('Enter New Notes Name');
            query="update notes set notes_name='{}' where s_no={}".format(notes_name,s_no);
            cursor.execute(query);
            self.connection.commit();
        elif upChoice == 2:
            notes_subject=input('Enter New Notes Subject Name');
            query="update notes set notes_name='{}' where s_no={}".format(notes_subject,s_no);
            cursor.execute(query);
            self.connection.commit();
        elif upChoice == 3:
            notes_content=input('Enter New Notes Content of Notes');
            query="update notes set notes_name='{}' where s_no={}".format(notes_content,s_no);
            cursor.execute(query);
            self.connection.commit();
        elif upChoice == 4:
            notes_description=input('Enter New Notes Description');
            query="update notes set notes_name='{}' where s_no={}".format(notes_description,s_no);
            cursor.execute(query);
            self.connection.commit();
        else:
           print('Press Valid Number');
    def deleteNotes(self,s_no):
        query="delete from notes where s_no={}".format(s_no);
        cursor=self.connection.cursor();
        cursor.execute(query);
        self.connection.commit();

# helper=NotesDatabaseHelper();
# helper.createNote(9,'discreate maths','Maths','hello world.. hello world.. hello world..hello world..hello world..','all given by teacher');
# helper.createNote(3,'discreate maths','Maths','hello world.. hello world.. hello world..hello world..hello world..','all given by teacher');
# helper.createNote(4,'discreate maths','Maths','hello world.. hello world.. hello world..hello world..hello world..','all given by teacher');
# helper.createNote(5,'discreate maths','Maths','hello world.. hello world.. hello world..hello world..hello world..','all given by teacher');
# helper.updateNotes(2)
# helper.deleteNotes(9)
# helper.showAllNotes()
