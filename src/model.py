from pydantic import BaseModel

# Create a Pydantic model for the request data
class CityData(BaseModel):
    city: str
    