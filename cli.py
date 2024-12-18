import sys
from models import AudioProducer, DigitalAudioWorkstation, session

def list_audio_producers():
    producers = session.query(AudioProducer).all()
    for producer in producers:
        print(f"ID: {producer.id}, Name: {producer.name}")

def list_workstations():
    workstations = session.query(DigitalAudioWorkstation).all()
    for workstation in workstations:
        print(f"ID: {workstation.id}, Name: {workstation.name}, Producer ID: {workstation.producer_id}")

def add_audio_producer(name):
    new_producer = AudioProducer(name=name)
    session.add(new_producer)
    session.commit()
    print(f"Audio Producer {name} added.")

def add_workstation(name, producer_id):
    producer = session.query(AudioProducer).filter_by(id=producer_id).first()
    if producer:
        new_workstation = DigitalAudioWorkstation(name=name, producer_id=producer.id)
        session.add(new_workstation)
        session.commit()
        print(f"Workstation {name} added for producer {producer.name}.")
    else:
        print("Producer not found.")

def delete_audio_producer(producer_id):
    producer = session.query(AudioProducer).filter_by(id=producer_id).first()
    if producer:
        session.delete(producer)
        session.commit()
        print(f"Audio Producer {producer.name} deleted.")
    else:
        print("Producer not found.")

def delete_workstation(workstation_id):
    workstation = session.query(DigitalAudioWorkstation).filter_by(id=workstation_id).first()
    if workstation:
        session.delete(workstation)
        session.commit()
        print(f"Workstation {workstation.name} deleted.")
    else:
        print("Workstation not found.")

def main():
    if len(sys.argv) < 2:
        print("Please provide a command.")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'list_producers':
        list_audio_producers()
    elif command == 'list_workstations':
        list_workstations()
    elif command == 'add_producer' and len(sys.argv) == 3:
        add_audio_producer(sys.argv[2])
    elif command == 'add_workstation' and len(sys.argv) == 4:
        add_workstation(sys.argv[2], int(sys.argv[3]))
    elif command == 'delete_producer' and len(sys.argv) == 3:
        delete_audio_producer(int(sys.argv[2]))
    elif command == 'delete_workstation' and len(sys.argv) == 3:
        delete_workstation(int(sys.argv[2]))
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
