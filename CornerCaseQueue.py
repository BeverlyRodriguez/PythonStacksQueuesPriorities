# This is for  correct order elements yet violates sort stability
# when comparing elements with equal priorities.
 
print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

from queues4 import PriorityQueue
from dataclasses import dataclass

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

#Comparison Operators
wipers < hazard_lights

messages = PriorityQueue()
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)


messages.dequeue()