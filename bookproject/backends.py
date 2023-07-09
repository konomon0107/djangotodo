from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # メールアドレスでユーザーを取得する
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # メールアドレスでユーザーが見つからない場合は、ユーザー名で検索する
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        # パスワードの検証
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
