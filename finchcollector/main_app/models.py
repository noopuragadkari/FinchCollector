from django.db import models

# Create your models here.
class Finch: 
  def __init__(self, name, description, lifespan):
    self.name = name
    self.description = description
    self.lifespan = lifespan

finches = [
  Finch('The Spice Finch', 'Is a sparrow-sized estrildid finch native to tropical Asia', 3),
  Finch('The Zebra Finch', 'The Australian zebra finch or chestnut-eared finch is the most common estrildid finch of Central Australia.', 2),
  Finch('The Strawberry Finch',' It is found in the open fields and grasslands of tropical Asia and is popular as a cage bird due to the colourful plumage of the males in their breeding season.', 3),
  Finch('Double-Barred Finch', 'The double-barred finch is an estrildid finch found in dry savannah.', 2)
]