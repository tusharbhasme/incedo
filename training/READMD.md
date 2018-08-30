Library Management using Python

Forms using HTML, Flat-file : json

Tasks to be performed : 

	1) Add Books
	2) Remove Books
	3) Add members
	4) Remove members
	5) Allocate Books to members
	6) DeAllocate Books to members


Flat-File Details :
	
	BOOKS --> Title, Author, Publication, Year, ISBN, No of same books

	MEMBER -->	User_Id, Name, Phone_No

	Issues --> issue_id, User_Id, ISBN, Start_Date, End_Date


Functions :

	Add books : Insert details of the books using a simple form that takes in all the data. If same ISBN, then +1 to no of same 			books column

	Remove books : Remove Books option --> Enter ISBN --> Remove --> Confirmation.
			 (If multiple books with same ISBN, then : Remove one book or Remove All option )

	Add Members: Insert details of the members using a simple form that takes in all the data. 

	Remove Members : Members --> Remove Members --> Enter User_Id --> Confirmation --> Remove

	Issueing :

		Allocation : Issueing --> Allocate --> Enter ISBN No, User_id, start_date, end_date. Generates issue_id on "Allocate" click --> -1 to no of same books

		DeAllocation : Issueing --> DeAllocate --> Enter issue_id/user_id :

		if issue_id --> check isbn no --> deaalocate --> confirm --> +1 to no of same books

		if user_id --> check issue history --> deallocate last entry --> confirm --> +1 to no of same books


Tips:
	Solution is expected to be OOPS based. 
	Please make use of map / decorators.
	Code should be PEP8 compliant.
	Please do proper error handling.
	Create your branch and include your name in it. Ex. bmanoj
