### DriverPython


Python Library to interface with angraDB

-----
#### Use

- Clone the repo or download the zip;
- Add the folder AngraDBPythonDriver to your project;
- Import the driver on your project with `from AngraDBPythonDriver import Driver`;

The first thing to be done is to instantiate a object of `Driver`. It receive two params for 
initialization, the `ip_address` and `ip_port` of the AngraDB server, an instantiation example would be 
`test_driver = Driver("127.0.0.1", 1234)`. The methods implemented for the object are the following:

##### create_db
`create_data_base(db_name)`

Creates a database with name `db_name`
##### connect
`connect_to_data_base(db_name)`

Connects to a database with name `db_name`
##### save
`save_document(document)`

Saves a document `document` and returns its key
##### lookup
`lookup_document(document_identification)`

Gets the document of key `document_identification`

##### update
`update_document(document_identification, new_document)`

Gets the document key `document_identification`, finds the corresponding document and updates it with the 
new document `new_document`

##### delete
`delete_document(document_identification)`

Gets the document key `document_identification`, finds the corresponding document and deletes it

---
#### Test

- Turn on AngraDB
- Run client_example.py (it runs a `create_db db`, a `connect db`, `save document` 
a `lookup id` a `update id document_update`, a `lookup id` and a `delete id` and prints all the server feedback on screen)


