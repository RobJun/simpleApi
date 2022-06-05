from signal import raise_signal
import requests

# validation of userId with external API
# true - when user exists
def validateId(userId : int) -> bool:
    url = 'https://jsonplaceholder.typicode.com/users/{:}'.format(userId)
    return bool(requests.get(url).status_code == 200)


#function to return posts from external API
#   userID -  used to retrieve user's posts
#   id - is id of a post
# if only post id is specified, function will return specific post
# if user ID is specified then if ID is specified it will return post only if the user has a post with the id
# otherwise (id is not specified) it will return an array of users posts
def getPost(userID : int = None ,id : int =None):
    if not userID and id:
        url = 'https://jsonplaceholder.typicode.com/posts/{:}'.format(id)
        res = requests.get(url)
        assert(res.status_code == 200)
        return res.json()
    elif userID:
        url = 'https://jsonplaceholder.typicode.com/users/{:}/posts'.format(userID)
        res = requests.get(url)
        assert(res.status_code == 200)
        body = res.json()
        if id: # find post with id within users posts
            for item in body:
                if item['id'] == id:
                    return item
            raise Exception("User({:}) doesn't own a post with id:{:}".format(userID,id))
        return body

    else:
        raise Exception('Atleast one of the parameters has to be specified')