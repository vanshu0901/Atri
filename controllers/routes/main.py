from .atri import Atri
from fastapi import Request, Response


def init_state(at: Atri):
#Assign .custom.values an array containing the choices you want the dropdown to display.
    
   pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass