import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Get the values from the query string or request body
        a = float(req.params.get('a', None))
        b = float(req.params.get('b', None))

        if a is None or b is None:
            return func.HttpResponse(
                "Please provide 'a' and 'b' as query parameters or in the request body",
                status_code=400
            )
        
        # Call the add function
        result = add(a, b)
        return func.HttpResponse(json.dumps({'result': result}), status_code=200)
    
    except ValueError:
        return func.HttpResponse(
            "Invalid input. Please ensure 'a' and 'b' are numbers.",
            status_code=400
        )

def add(a, b):
    """Function that adds two numbers."""
    return a + b
