from AngraDBPythonDriver import Driver

test_driver = Driver("127.0.0.1", 1234)
response = test_driver.create_data_base("db")
print response
response = test_driver.connect_to_data_base("db")
print response
doc_key = test_driver.save_document("document")
print doc_key
response = test_driver.lookup_document(doc_key)
print response
response = test_driver.update_document(doc_key, "document_update")
print response
response = test_driver.lookup_document(doc_key)
print response