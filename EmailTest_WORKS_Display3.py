import csv
import os
import win32com.client as win32
olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')
with open('./dist_foa_coco.csv','r')as who_where:
    csv_reader = csv.reader(who_where)
    next(csv_reader)
    for row in csv_reader:
        mail_item = olApp.CreateItem(0)
        coco_email = row[2]
        district = row[0]
        body = "Hello! "+row[3]+" How are you! This is just for testing."
        #mail_item.Sender = "Contact@a.hall.win"
        mail_item.to = row[2]
        attachment_prefix = row[0]
        # find all files in the current directory that start with the attachment prefix
        attachment_files = []
        for file_name in os.listdir('.'):
            if file_name.startswith(attachment_prefix):
                attachment_files.append(os.path.abspath(file_name))

        if attachment_files:
            outlook = win32.Dispatch('Outlook.Application')
            message = outlook.CreateItem(0)

            # set message properties
            message.To = coco_email
            message.Subject = district
            message.Body = body

            # attach all matching files
            for attachment_file in attachment_files:
                attachment = message.Attachments.Add(attachment_file)
       
        mail_item.Display()



