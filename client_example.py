from PythonDriver import Driver


test_driver = Driver("127.0.0.1", 1234)
response = test_driver.create_data_base("db")
print response
response = test_driver.connect_to_data_base("db")
print response
