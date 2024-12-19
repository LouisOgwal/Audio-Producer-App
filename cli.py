import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, AudioProducer, DigitalAudioWorkstation 
from tabulate import tabulate 

# Database URL (you can change this to your desired database)
DATABASE_URL = "sqlite:///audio_producer_app.db"

# Set up engine and session
engine = create_engine(DATABASE_URL, echo=True) 
Session = sessionmaker(bind=engine)
session = Session()

# Initialize the database
def init_database():
    """Initialize the database by creating tables."""
    try:
        # Check if tables already exist before creating
        Base.metadata.create_all(engine)
        print("Database created and tables initialized.")
    except Exception as e:
        print(f"Error during initialization: {e}")

# Create a new audio producer
def create_audio_producer():
    """Create a new audio producer."""
    name = input("Enter Audio Producer's name: ")
    audio_producer = AudioProducer(name=name)
    try:
        session.add(audio_producer)
        session.commit()
        print(f"Audio Producer '{name}' created successfully with ID: {audio_producer.id}")
    except Exception as e:
        session.rollback()
        print(f"Error creating Audio Producer: {e}")

# Update audio producer details
def update_audio_producer():
    """Update audio producer details."""
    producer_id = int(input("Enter Audio Producer's ID to update: "))
    producer = session.query(AudioProducer).filter(AudioProducer.id == producer_id).first()

    if producer:
        print(f"Updating details for Producer: {producer.name}")
        new_name = input(f"Enter new name (current: {producer.name}): ") or producer.name
        producer.name = new_name
        try:
            session.commit()
            print(f"Audio Producer {producer.name} updated successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error updating Audio Producer: {e}")
    else:
        print("Audio Producer with that ID not found.")

# Delete an audio producer
def delete_audio_producer():
    """Delete an audio producer."""
    producer_id = int(input("Enter Audio Producer's ID to delete: "))
    producer = session.query(AudioProducer).filter(AudioProducer.id == producer_id).first()

    if producer:
        try:
            session.delete(producer)
            session.commit()
            print(f"Audio Producer with ID {producer_id} deleted successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting Audio Producer: {e}")
    else:
        print("Audio Producer with that ID not found.")

# List all audio producers
def list_audio_producers():
    """List all audio producers."""
    producers = session.query(AudioProducer).all()
    if producers:
        
        table_data = [['ID', 'Name']]  
        for producer in producers:
            table_data.append([producer.id, producer.name])

        # Print the table using tabulate
        print(tabulate(table_data, headers='firstrow', tablefmt='grid'))
    else:
        print("No audio producers found.")

# Create a new digital audio workstation
def create_workstation():
    """Create a new digital audio workstation."""
    name = input("Enter Workstation's name: ")
    producer_id = int(input("Enter Audio Producer's ID for this workstation: "))
    
    producer = session.query(AudioProducer).filter(AudioProducer.id == producer_id).first()
    if producer:
        workstation = DigitalAudioWorkstation(name=name, audio_producer_id=producer.id)
        try:
            session.add(workstation)
            session.commit()
            print(f"Workstation '{name}' created successfully under Producer '{producer.name}'")
        except Exception as e:
            session.rollback()
            print(f"Error creating Workstation: {e}")
    else:
        print(f"Audio Producer with ID {producer_id} not found. Workstation creation failed.")

# Update workstation details
def update_workstation():
    """Update workstation details."""
    workstation_id = int(input("Enter Workstation ID to update: "))
    workstation = session.query(DigitalAudioWorkstation).filter(DigitalAudioWorkstation.id == workstation_id).first()

    if workstation:
        print(f"Updating details for Workstation: {workstation.name}")
        new_name = input(f"Enter new name (current: {workstation.name}): ") or workstation.name
        workstation.name = new_name
        try:
            session.commit()
            print(f"Workstation {workstation.name} updated successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error updating Workstation: {e}")
    else:
        print("Workstation with that ID not found.")

# Delete a workstation
def delete_workstation():
    """Delete a workstation."""
    workstation_id = int(input("Enter Workstation ID to delete: "))
    workstation = session.query(DigitalAudioWorkstation).filter(DigitalAudioWorkstation.id == workstation_id).first()

    if workstation:
        try:
            session.delete(workstation)
            session.commit()
            print(f"Workstation with ID {workstation_id} deleted successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting Workstation: {e}")
    else:
        print("Workstation with that ID not found.")

# List all workstations
def list_workstations():
    """List all workstations."""
    workstations = session.query(DigitalAudioWorkstation).all()
    if workstations:
        # Using tabulate to format the output as a table
        table_data = [['ID', 'Name', 'Producer ID']]
        for workstation in workstations:
            table_data.append([workstation.id, workstation.name, workstation.audio_producer_id])

        # Print the table using tabulate
        print(tabulate(table_data, headers='firstrow', tablefmt='grid'))
    else:
        print("No workstations found.")

# Main Menu Function
def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nWelcome to the Audio Production System!")
        print("1. Add a new Audio Producer")
        print("2. Update Audio Producer details")
        print("3. Delete Audio Producer details")
        print("4. List all Audio Producers")
        print("5. Add a new Workstation")
        print("6. Update Workstation details")
        print("7. Delete Workstation details")
        print("8. List all Workstations")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_audio_producer()
        elif choice == "2":
            update_audio_producer()
        elif choice == "3":
            delete_audio_producer()
        elif choice == "4":
            list_audio_producers()
        elif choice == "5":
            create_workstation()
        elif choice == "6":
            update_workstation()
        elif choice == "7":
            delete_workstation()
        elif choice == "8":
            list_workstations()
        elif choice == "9":
            print("Thank you for using the Audio Production System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    init_database()  
    main_menu() 
