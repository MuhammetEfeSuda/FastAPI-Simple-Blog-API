from fastapi import APIRouter, HTTPException
from models.post import Post, Postcreate, Postupdate
from config.db import conn
from schemas.post import postEntity, postsEntity
from bson import ObjectId
from datetime import datetime, timedelta
from pydantic import ValidationError

post = APIRouter()

@post.get('/', tags=["Posts"])
async def find_all_posts():
    posts = postsEntity(conn.Project.post.find())
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts

@post.get('/{id}', tags=["Posts"])
async def find_one_post(id: str):
    try:
        post_data = conn.Project.post.find_one({"_id": ObjectId(id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid post ID format")
    
    if post_data:
        return postEntity(post_data)
    raise HTTPException(status_code=404, detail="Post not found")

@post.post('/', tags=["Posts"])
async def create_post(post: Postcreate):
    if len(post.title) < 3 or len(post.title) > 30:
        raise HTTPException(status_code=422, detail="Title must be between 3 and 30 characters.")
    
    if len(post.short_description) > 50:
        raise HTTPException(status_code=422, detail="Short description must be at most 50 characters.")
    
    if len(post.description) > 500:
        raise HTTPException(status_code=422, detail="Description must be at most 500 characters.")
    
    new_post = dict(post)
    now_utc = datetime.utcnow()
    now_utc_plus_3 = now_utc + timedelta(hours=3)
    new_post["create_date"] = now_utc_plus_3
    new_post["update_date"] = now_utc_plus_3

    try:
        inserted_post = conn.Project.post.insert_one(new_post)
        created_post = conn.Project.post.find_one({"_id": inserted_post.inserted_id})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Post could not be created")
        
    return postEntity(created_post)

@post.put('/{id}', tags=["Posts"])
async def update_post(id: str, post: Postupdate):
    if len(post.title) < 3 or len(post.title) > 30:
        raise HTTPException(status_code=422, detail="Title must be between 3 and 30 characters.")
    
    if len(post.short_description) > 50:
        raise HTTPException(status_code=422, detail="Short description must be at most 50 characters.")
    
    if len(post.description) > 500:
        raise HTTPException(status_code=422, detail="Description must be at most 500 characters.")

    try:
        now_utc_plus_3 = datetime.utcnow() + timedelta(hours=3)
        updated_post = conn.Project.post.find_one_and_update(
            {"_id": ObjectId(id)}, 
            {"$set": {**dict(post), "update_date": now_utc_plus_3}}, 
            return_document=True
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid post ID format")
    
    if updated_post:
        return postEntity(updated_post)
    raise HTTPException(status_code=404, detail="Post not found")

@post.delete('/{id}', tags=["Posts"])
async def delete_post(id: str):
    try:
        deleted_post = conn.Project.post.find_one_and_delete({"_id": ObjectId(id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid post ID format")
    
    if deleted_post:
        return postEntity(deleted_post)
    raise HTTPException(status_code=404, detail="Post not found")
