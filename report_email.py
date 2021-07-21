#!/usr/bin/env python3
"""Script to process supplier fruit description data from
supplier-data/descriptions directory

Content of report should look like the following:
    Processed Update on <Today's date>
    [blank line]
    name: Apple
    weight: 500 lbs
    [blank line]
    name: Avocado
    weight: 200 lbs
    [blank line]
    ...
"""
import os, reports, emails
from datetime import date

def main():
    # Name of report to generate
    attachment = '/tmp/processed.pdf'

    # Get date for title
    today = date.today()
    title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))

    # Get files from directory to iterate
    path = 'supplier-data/descriptions/'
    files = os.listdir(path)
    paragraph = ''  # Empty paragraph

    # Open files and add fruit name and weight to paragraph
    for file in files:
        if os.path.splitext(file)[1] != '.txt':
            continue

        with open(path + file) as fp:
            for i, line in enumerate(fp):
                if i == 0:
                    paragraph += 'Name: {}'.format(line)
                elif i == 1:
                    paragraph += 'Weight: {}'.format(line)
            paragraph += '\n'

    # Replace newlines with breaks
    paragraph = paragraph.replace('\n', '<br/>')

    # Generate report
    reports.generate_report(attachment, title, paragraph)

    # Send PDF report as an email attachment
    sender = 'automation@example.com'
    receiver = '<username>@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = '''All fruits are uploaded to our website successfully. A detailed
    list is attached to this email.'''
    message = emails.generate_email(
            sender, receiver, subject, body, attachment)
    emails.send_email(message)

if __name__ == "__main__":
    main()
