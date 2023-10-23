"""
model.py: Model contains the model or schema for certain
payloads or responses for specific endpoints
"""
from pydantic import BaseModel

# Create a Pydantic model for the request data
class CityData(BaseModel):
    """City Data"""
    city: str
    