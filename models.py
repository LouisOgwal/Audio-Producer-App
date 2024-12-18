from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# Define the AudioProducer model
class AudioProducer(Base):
    __tablename__ = 'audio_producers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    digital_audio_workstations = relationship('DigitalAudioWorkstation', back_populates='audio_producer')

    def __repr__(self):
        return f'<AudioProducer(id={self.id}, name="{self.name}")>'


# Define the DigitalAudioWorkstation model
class DigitalAudioWorkstation(Base):
    __tablename__ = 'digital_audio_workstations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    audio_producer_id = Column(Integer, ForeignKey('audio_producers.id'))
    audio_producer = relationship('AudioProducer', back_populates='digital_audio_workstations')

    def __repr__(self):
        return f'<DigitalAudioWorkstation(id={self.id}, name="{self.name}")>'


# Create an engine to connect to the database
engine = create_engine('sqlite:///audio_producer.db')  # You can change this to the appropriate database URL

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()
