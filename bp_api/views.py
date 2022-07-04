import logging
from typing import Optional

from flask import Blueprint, jsonify, abort

from bp_posts.dao.comment import Comment
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from bp_posts.dao.comment_dao import CommentDAO

from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

#Создаем блупринт
bp_api = Blueprint("bp_api", __name__)

# Создаем обьекты доступа к данным
post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")


@bp_api.route('/posts/')
def api_posts_all():
    """Этдпоинт для всех постов"""
    all_posts: list[Post] = post_dao.get_all()
    all_posts_as_dicts: list[dict] = [post.as_dict() for post in all_posts]
    api_logger.debug("Запрошены все посты")
    return jsonify(all_posts_as_dicts), 200

@bp_api.route('/posts/<int:pk>/')
def api_posts_single(pk: int):
    """Этдпоинт для одного постоа"""
    post: Optional[Post] = post_dao.get_by_pk(pk)
    if post is None:
        abort(404)

    return jsonify(post.as_dict()), 200

@bp_api.errorhandler(404)
def api_error_404(error):
    return jsonify({"error": str(error)}), 404

@bp_api.route('/')
def api_posts_hello():

    return "Это фпи. Доступные эндпоинты /api/posts и  /api/posts/<pk>. " \
           "Смотри документацию у меня на гитхабе"


