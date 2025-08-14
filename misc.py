import json, os


#Import json
def get_project_settings(import_filepath):
    """ 
    #Functon to import settings from settings.json
    param: path to settings.json
    return: settings as a dict object
    """
    #check if path exists
    if os.path.exists(import_filepath):
        #if yes, import file path
        f = open(import_filepath, "r")
        
        #read the file 
        project_settings = json.load(f)
        
        #close file
        f.close()

        #return project settings 
        return project_settings

    else: #if it does not exist
        raise ImportError('settings.json does not exist at provided location')

