from bp_posts.dao.comment_dao import CommentDAO

cd = CommentDAO("data/comments.json")

print(cd.get_comments_by_post_pk(2))
