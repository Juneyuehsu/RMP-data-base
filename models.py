from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///display_models.db')

class GD_All(Base):
    __tablename__ = 'gd_all'
    id = Column(Integer, primary_key=True)
    resolution_n = Column(String)
    resolution_x = Column(Integer)
    resolution_y = Column(Integer)
    size = Column(Float)
    aspect_ratio = Column(String)
    panel_type = Column(String)
    ppi = Column(Float)
    model_name = Column(String)
    brightness = Column(Integer)
    viewangle_h = Column(Integer)
    viewangle_v = Column(Integer)
    temp_l = Column(Integer)
    temp_h = Column(Integer)
    led_life = Column(Integer)
    color_bit = Column(String)
    led_driver = Column(String)
    interface = Column(String)
    color = Column(String)
    note = Column(String)
    status = Column(String)

Base.metadata.create_all(engine)
