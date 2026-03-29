from pydantic import BaseModel, Field
from typing import Optional

# This defines the "Hands" of the robot (Actions)
class Action(BaseModel):
    command: str = Field(description="The type of action, e.g., 'click' or 'type'")
    target: str = Field(description="The ID of the button or input field")
    value: Optional[str] = Field(default=None, description="The text to type, if any")

# This defines the "Eyes" of the robot (Observations)
class Observation(BaseModel):
    screenshot: str = Field(description="Base64 string or URL of the screen image")
    text_content: str = Field(description="The text data from the expense report")
    reward: float = Field(default=0.0, description="The score from 0.0 to 1.0")
    done: bool = Field(default=False, description="Whether the task is finished")