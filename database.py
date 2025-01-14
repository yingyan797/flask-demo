import sqlite3

class Database:
    def __init__(self, name):
        self.name = name
    def start(self):
        self.con = sqlite3.connect(self.name)

    def create_table(self, schema):
        for tname, cols in schema.items():
            instr = f"create table if not exists {tname} ("
            for cname, ctype in cols:
                instr += f"{cname} {ctype}, "
            instr = instr[:-2]+")"
            self(instr)

    def __call__(self, instr):
        print(" * Executing:", instr)
        return self.con.execute(instr)
    
SCHEMA = {
    "employee": [("name", "TEXT"), ("department", "TEXT"), ("years", "Integer"), ("salary", "Integer")],
    # float: Real/REAL
    "department": [("name", "TEXT"), ("location", "Integer"), ("capacity", "Integer")]
}


if __name__ == "__main__":
    db = Database("data.db")
    print("The database is called:", db.name)
    db.start()
    db.create_table(SCHEMA)

    # Insert entries to both tables
    for en, ed, ey, es in [("Andy", "Engineering", 5, 50000), 
                           ("Tarkhan", "Marketing", 4, 40000),
                           ("David", "Engineering", 2, 45000), 
                           ("Sam", "Marketing", 3, 42000),
                           ]:
        db(f"insert into employee (name, department, years, salary) values ('{en}', '{ed}', {ey}, {es})")
    
    for dn, dl, dc in [("Engineering", 205, 20), 
                       ("Marketing", 101, 15)]:
        db(f"insert into department (name, location, capacity) values ('{dn}', {dl}, {dc})")
    
    # Show table content
    print(db("select name, salary from employee").fetchall())

    # Delete table entry
    db("delete from employee where name='Sam'")

    # Update table content
    db("update employee set salary=salary+1000 where name='Tarkhan'")

    # Show table content after change, matching conditions
    print(db("select name, salary from employee").fetchall())
    print(db("select name, salary from employee where years > 3").fetchall())
    print("Left join table:", db("select employee.name, department.location, salary from employee left join department on employee.department = department.name").fetchall())

    # db.con.commit()
