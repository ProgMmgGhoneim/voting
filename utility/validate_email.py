import re
 
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
def check_email(email: str):
    """
        Validate sent Email
    """
    if(re.fullmatch(email_regex, email)):
        return True
    else:
        return False