from api_helpers import drive_helpers

def get_all_drives(event, context):
    print(event)
    print(context)
    
    data = drive_helpers.get_all_drives()
    return data
