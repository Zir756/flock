from django.contrib import admin
from .models import Post, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

from .models import Memo          # Memo をインポート

# Register your models here.

admin.site.register(Memo)         # 追加

from .models import Todo          # Todo をインポート

# Register your models here.

admin.site.register(Todo)         # 追加