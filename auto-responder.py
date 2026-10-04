def smart_respond(email_body):
    email_lower = email_body.lower()
    if 'broken' in email_lower or 'damaged' in email_lower:
        return 'ACTION: Generate refund/replacement email template.'
    elif 'tracking' in email_lower:
        return 'ACTION: Fetch tracking API and reply.'
    return 'ACTION: Forward to human support.'

if __name__ == '__main__':
    print(smart_respond('My package arrived but the item is completely broken!'))