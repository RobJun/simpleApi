


#required fields is tuple of tuples containing name of the field, type and boolean specifing Hard error
# Hard error is raised when required field isn't in request body or field content error
# Soft error is raised only when content error appears (when types are diffrent)
def checkInputData(data : dict, requiredFields: tuple = (('id',int,True),('userId',int,True),('title',str,False),('body',str,False))):
    for attribute,typ,hardError in requiredFields:
        if(attribute in data and isinstance(data[attribute],typ)):
            if(isinstance(data[attribute],str)):
                if(len(data[attribute]) == 0):
                    raise Exception("Field {:} cannot be empty".format(attribute))
            elif(isinstance(data[attribute],int)):
                if(data[attribute] < 0):
                    raise Exception("Field {:} must be large than 0".format(attribute))
        else:
            if hardError:
                raise Exception("request json doesn't contain requierd field {:} or is wrong type (given: {:}, required: {:})".format(attribute,type(data[attribute]),typ))



