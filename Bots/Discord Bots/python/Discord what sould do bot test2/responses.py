def get_response(message:str) -> str:
    p_message = message.lower()

    match p_message:
        case 'hello':
            return "Hi! there!"
        case 'ping':
            return "pong"
        case "way":
            return "let's start"
    
    return "command not found"
