from flask import current_app as app
from paralympics.schemas import RegionSchema, EventSchema
from paralympics import db
from paralympics.models import Region, Event

# Flask-Marshmallow Schemas
regions_schema = RegionSchema(many=True)
region_schema = RegionSchema()
events_schema = EventSchema(many=True)
event_schema = EventSchema()

@app.route('/')
def hello():
    return f"Hello!"

@app.get("/regions")
def get_regions():
    """Returns a list of NOC region codes and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_regions = db.session.execute(db.select(Region)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = regions_schema.dump(all_regions)
    # Return the data
    return result

@app.get('/events')
def get_events():
    """Returns a list of events and their details in JSON."""
    # Select all the events using Flask-SQLAlchemy
    all_events = db.session.execute(db.select(Event)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = events_schema.dump(all_events)
    # Return the data
    return result

@app.get('/events/<int:event_id>')
def get_event(event_id):
    """Returns the details of a single event in JSON."""
    # Select the event using Flask-SQLAlchemy
    event = db.session.execute(db.select(Event).filter(Event.id == event_id)).scalar()
    # Get the data using Marshmallow schema (returns JSON)
    result = event_schema.dump(event)
    # Return the data
    return result

@app.get('/regions/<string:NOC>')
def get_region(NOC):
    """Returns the details of a single region in JSON."""
    # Select the region using Flask-SQLAlchemy
    region = db.session.execute(db.select(Region).filter(Region.NOC == NOC)).scalar()
    # Get the data using Marshmallow schema (returns JSON)
    result = region_schema.dump(region)
    # Return the data
    return result
