import psycopg2
import sys
def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="iti_python",
            user="nad",
            password="nada@@@999",
        )
        
        print("Connected to the database successfully")
      
        return connection
    except:
        print(f"Error connecting to the database")
        return None
# continue_db = connect_db()
# print(continue_db())
print(connect_db())

def insert_db(name, age, track_id):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        insert_query = f"insert into trainee (name, age, track_id) values ('{name}', {age}, {track_id});"
        cursor.execute(insert_query)
        connection.commit()
        
        print("insert")
      
    except psycopg2.DatabaseError as e:
        print(f"Error inserting trainee: {e}")
    finally:
        cursor.close()
        connection.close()


insert_db("nada", 23, 1)


# step 3: update
def update_db(trainee_id, name, age, track_id):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        update_query = f"UPDATE trainee SET name = '{name}', age = {age}, track_id = {track_id}  WHERE id = {trainee_id};"
        cursor.execute(update_query)
        connection.commit()
        print(f"trainee with ID {trainee_id} updated.")
    except psycopg2.DatabaseError as e:
        print(f"Error updating trainee: {e}")
    finally:
        cursor.close()
        connection.close()


update_db(1, "mohamed", 25, 1)


# step 4: select
def select_db():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        select_query = "SELECT * FROM trainee;"
        cursor.execute(select_query)
        employees = cursor.fetchall()

        for employee in employees:
            print(f"# {employee}")
    except:
        print(f"Error select trainee")
    finally:
        cursor.close()
        connection.close()


select_db()


# step 5: delete
def delete_db(trainee_id):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        delete_query = f"DELETE FROM trainee WHERE id = {trainee_id};"
        cursor.execute(delete_query)
        connection.commit()

        print(f"Employee with ID {trainee_id} deleted.")
    except:
        print(f"Error deleting trainee")
    finally:
        cursor.close()
        connection.close()


delete_db(3)


# =================================================================================================
# =================================================================================================


class Human:
    class_var = "Human Class Variable"

    def _init_(self, name, age):
        self.instance_var_name = name
        self.instance_var_age = age

    def speak(self):
        return f"({self.instance_var_name}) says hello!"

    def introduce(self):
        return f"Hello, my name is ({self.instance_var_name}) and I am ({self.instance_var_age}) years old."

    @classmethod
    def get_class_var(cls):
        return cls.class_var + " edit."


nadamohamed = Human('nada', 23)
print(nadamohamed.speak())
print(nadamohamed.introduce())
print(nadamohamed.get_class_var())


class Employee:
    class_var = "Employee Class Variable"

    def _init_(self, name, age, employee_id):
        self.instance_var_name = name
        self.instance_var_age = age
        self.instance_var_employee_id = employee_id

    def work(self):
        return f"Employee ({self.instance_var_name}) with ID ({self.instance_var_employee_id}) is working."

    @classmethod
    def get_class_var(cls):
        return cls.class_var + " edit."


nadamm = Employee("nada", 23, 1)
print(nadamm.work())
print(nadamm.get_class_var())