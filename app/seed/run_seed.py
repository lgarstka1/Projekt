import os
import time

from src.app import app, db, Task

def run_seed():
    print("Rozpoczynam seedowanie bazy danych...")
    
    
    time.sleep(5)
   
    with app.app_context():
           db.create_all()

        
        if Task.query.count() == 0:
            zadania = [
                Task(name="Task1"),
                Task(name="Task2"),
                Task(name="Task3"),
                Task(name="Task4"),
                Task(name="Task5")
            ]
            db.session.bulk_save_objects(zadania)
            db.session.commit()
            print("Dodano 5 tasków")
        else:
            print("Baza z danymi")

        output_dir = "/app/seed_output"
        os.makedirs(output_dir, exist_ok=True)
        
        
        with open(f"{output_dir}/seed.log", "w", encoding="utf-8") as log_file:
            log_file.write("Seedowanie zakonczone sukcesem.\n")
            log_file.write("Dodano 5 zadan do tabeli Task.\n")
            
     
        with open(f"{output_dir}/tasks.csv", "w", encoding="utf-8") as csv_file:
            csv_file.write("id,name\n")
 
            for t in Task.query.all():
                csv_file.write(f"{t.id},{t.name}\n")
                
        print(f"Pliki seedera zostaly poprawnie wygenerowane w {output_dir}")

if __name__ == '__main__':
    run_seed()