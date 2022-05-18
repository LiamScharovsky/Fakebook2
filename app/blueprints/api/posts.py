from .import bp as posts
from app.blueprints.blog.models import Post 
from flask import jsonify, request                           #turns data into java script
from app import db


@posts.route('/posts', methods=['GET'])             #gets all posts
def getPosts():
    """ 
    [GET] /api/v1/posts                             
    """
    posts=[p.toDict() for p in Post.query.all()]
    return jsonify(posts)                           # make post java script

@posts.route('/posts/<id>', methods=['GET'])
def getOnePosts(id):
    """
    [GET] /api/v1/posts/<id>
    """
    return jsonify(Post.query.get(id).toDict())     #returns 1 post based on ID
                           # make post java script    @posts.route('/posts', methods=['GET'])
@posts.route('/posts', methods=['POST'])
def createPosts():
    """
    [POST] /api/v1/posts
    """    
    response = request.get_json()               #get data
    post = Post()                               #make new post
    post.fromDict(response)                     #instanciate post
    db.session.add(post)                        #add it to the database
    db.session.commit()
    #posts=[p.toDict() for p in Post.query.all()]
    return jsonify(post.toDict())                           # make post java script


@posts.route('/posts/<id>', methods=['PUT'])
def updatePosts(id):
    """
    [PUT] /api/v1/posts/<id>
    """    
    response = request.get_json()                       #get request from json
    post=Post.query.get(id)                             #get post json is asking for
    post.body = response.get('body')                    #change the body
    db.session.add(post)
    db.session.commit()                                 #put it in the database
    return jsonify(post.toDict())                           # make post java script



@posts.route('/posts/<id>', methods=['DELETE'])
def deletePosts(id):
    """
    [DELETE] /api/v1/posts/<id>
    """
    post=Post.query.get(id)                             #get post by id
    db.session.delete(post)                             #delete it
    db.session.commit()                                 #commit
    return ({"message" : "Post Deleted"})                   #confirm
