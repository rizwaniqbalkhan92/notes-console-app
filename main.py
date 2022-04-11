from helper import NotesDatabaseHelper ;

methods=NotesDatabaseHelper();
# def main():
while True:
    print("Press 1 for 'Create Notes '   \n  Press 2 for 'Update Notes ' \n Press 3 for 'Delete Notes ' \n Press 4 for 'Read Notes' \n  Press 5 for 'Exit'");
    try:
        number=int(input('Enter Number : '));
        if number==1:
            id=int(input('Enter Notes Id : '));

            notes_name=input('Enter Notes Name : ')
            notes_subject=input('Enter Notes Subject : ')
            notes_content=input('Enter Notes Content : ')
            notes_description=input('Enter Notes Description : ')
            methods.createNote(id,notes_name,notes_subject,notes_content,notes_description);
        elif number==2:
            id=int(input('Enter Notes Id for update : '));

            methods.updateNotes(id);
        elif number==3:
            id=int(input('Enter Notes Id : '));
            methods.deleteNotes(id);
        elif number==4:
            methods.showAllNotes();
        elif number==5:
            break;
    except Exception as e:
            print(e)

