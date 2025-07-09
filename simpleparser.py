import re

def parse_resume(text):
    # Split lines and remove empty ones
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # Assume first non-empty line is the name
    name = lines[0] if lines else 'Not found'

    # Find email using regex
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    email_match = re.search(email_pattern, text)
    email = email_match.group() if email_match else 'Not found'

    # Find phone number using regex (simple pattern for international or local formats)
    phone_pattern = r'(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'
    phone_match = re.search(phone_pattern, text)
    phone = phone_match.group() if phone_match else 'Not found'

    # Extract skills (look for line starting with 'Skills' or 'SKILLS')
    skills = []
    skills_section_found = False
    for line in lines:
        if skills_section_found:
            if line.lower().startswith('experience') or ':' in line:
                break
            skills.extend([skill.strip() for skill in line.split(',')])
        elif line.lower().startswith('skills'):
            skills_section_found = True
            if ':' in line:
                skills_part = line.split(':', 1)[1]
                skills.extend([skill.strip() for skill in skills_part.split(',')])
    
    return {
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Skills': skills or ['Not found']
       

    }

# Sample usage
resume_text = """
Chiza
Bayantasha jambutu
warmachine001@gmail.com
+234 8049139903

Summary
Experienced software engineer...

Skills: Python, JavaScript, HTML, CSS, Git,Tiktok


"""

parsed = parse_resume(resume_text)
for key, value in parsed.items():
    print(f"{key}: {value}")