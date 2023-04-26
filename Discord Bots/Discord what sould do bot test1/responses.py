def get_response(message:str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hi'
    if p_message == '!help':
        return "`this is help!`"
    
    return "command not found"
