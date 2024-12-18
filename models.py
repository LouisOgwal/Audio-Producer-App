from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class AudioProducer(Base):
    __tablename__ = 'audio_producers'  # Corrected tablename syntax

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship with DigitalAudioWorkstation
    digital_audio_workstations = relationship('DigitalAudioWorkstation', back_populates='audio_producer')

    def __repr__(self):  # Corrected repr syntax
        return f'<AudioProducer(id={self.id}, name="{self.name}")>'


class DigitalAudioWorkstation(Base):
    __tablename__ = 'digital_audio_workstations'  # Corrected tablename syntax

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # ForeignKey for the relationship with AudioProducer
    audio_producer_id = Column(Integer, ForeignKey('audio_producers.id'))

    # Define the relationship back to AudioProducer
    audio_producer = relationship('AudioProducer', back_populates='digital_audio_workstations')

    def __repr__(self):  # Corrected repr syntax
        return f'<DigitalAudioWorkstation(id={self.id}, name="{self.name}")>'
