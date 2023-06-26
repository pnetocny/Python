import mysql.connector

# Připojení k databázi
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="todo_list"
)

# Vytvoření tabulky 'tasks', pokud ještě neexistuje
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255))")

# Funkce pro vytvoření nového úkolu
def create_task(task):
    sql = "INSERT INTO tasks (task) VALUES (%s)"
    val = (task,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Úkol vytvořen.")

# Funkce pro zobrazení všech úkolů
def display_tasks():
    mycursor.execute("SELECT * FROM tasks")
    tasks = mycursor.fetchall()
    if tasks:
        print("Seznam úkolů:")
        for task in tasks:
            print(task[0], task[1])
    else:
        print("Žádné úkoly nejsou k dispozici.")

# Funkce pro aktualizaci úkolu
def update_task(task_id, new_task):
    sql = "UPDATE tasks SET task = %s WHERE id = %s"
    val = (new_task, task_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Úkol aktualizován.")

# Funkce pro odstranění úkolu
def delete_task(task_id):
    sql = "DELETE FROM tasks WHERE id = %s"
    val = (task_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Úkol odstraněn.")

# Hlavní funkce programu
def main():
    while True:
        print("\n--- Správce úkolů ---")
        print("1. Vytvořit úkol")
        print("2. Zobrazit úkoly")
        print("3. Aktualizovat úkol")
        print("4. Odstranit úkol")
        print("5. Konec")

        choice = input("Zadejte volbu: ")

        if choice == "1":
            task = input("Zadejte název úkolu: ")
            create_task(task)
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            task_id = input("Zadejte ID úkolu k aktualizaci: ")
            new_task = input("Zadejte nový název úkolu: ")
            update_task(task_id, new_task)
        elif choice == "4":
            task_id = input("Zadejte ID úkolu k odstranění: ")
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Neplatná volba.")

    # Uzavření spojení s databází při ukonč


