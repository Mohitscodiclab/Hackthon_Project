import re
import os

def redact_sensitive_info(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    redaction_counts = {
        'email': 0,
        'phone': 0,
        'credit_card': 0,
        'ssn': 0
    }

    # Redact Emails
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    content, count = re.subn(email_pattern, '[REDACTED]', content)
    redaction_counts['email'] = count

    # Redact Phone Numbers (US and Intl)
    phone_pattern = r'(\+?\d{1,3}[\s-]?)?(\(?\d{3}\)?[\s-]?)\d{3}[\s-]?\d{4}'
    content, count = re.subn(phone_pattern, '[REDACTED]', content)
    redaction_counts['phone'] = count

    # Redact Credit Card Numbers
    credit_card_pattern = r'\b(?:\d[ -]*?){13,16}\b'
    content, count = re.subn(credit_card_pattern, '[REDACTED]', content)
    redaction_counts['credit_card'] = count

    # Redact SSNs (Social Security Numbers)
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    content, count = re.subn(ssn_pattern, '[REDACTED]', content)
    redaction_counts['ssn'] = count

    # Save redacted output
    output_path = os.path.join(os.path.dirname(file_path), 'redacted_output.txt')
    with open(output_path, 'w') as output_file:
        output_file.write(content)

    # Create log file
    log_path = os.path.join(os.path.dirname(file_path), 'redaction_log.txt')
    with open(log_path, 'w') as log_file:
        for key, value in redaction_counts.items():
            log_file.write(f'{key.capitalize()}s Redacted: {value}\n')

    print("✅ Redaction completed.")
    print(f"🔒 Redacted file saved at: {output_path}")
    print(f"📊 Redaction log saved at: {log_path}")

# Example usage
if __name__ == "__main__":
    file_path = 'text.txt'  # Replace with your input file
    redact_sensitive_info(file_path)
