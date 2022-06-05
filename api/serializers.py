from django.db.models import QuerySet

def serializePosts(data,many : bool= False,concate : dict = None) -> dict:
    if not data: return None
    if isinstance(data,dict) or isinstance(data,list):
        return data
    if many:
        result = [{'id':row.id,'userId': row.userId, 'title': row.title, 'body': row.body} for row in data]
        if concate:
            res = (result + concate)
            result = { frozenset(item.items()) : item for item in res}.values()
        return result
    else:
        
        if(isinstance(data,QuerySet)):
            return  {'id':data[0].id,'userId': data[0].userId, 'title': data[0].title, 'body': data[0].body}
        else:
            return  {'id':data.id,'userId': data.userId, 'title': data.title, 'body': data.body}


