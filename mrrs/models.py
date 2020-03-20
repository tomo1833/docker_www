from django.db import models
from django.utils import timezone

class room_info (models.Model):
    """
    room_infoテーブルのモデル.

    """
    # 会議室ID : INTEGER型
    room_id = models.IntegerField(primary_key=True)
    # 会議室名 : 文字列型30桁
    room_name = models.CharField(max_length=30)
    # 削除フラグ : INTEGER型
    del_flg = models.IntegerField()    

    def __str__(self):
        return u'%s' % (self.room_id)

class room_reservation (models.Model):
    """
    room_reservationテーブルのモデル.

    """
    # id : INTEGER型で、主キー
    id = models.IntegerField(primary_key=True)
    # 会議室ID : INTEGER型
    room_id=models.ForeignKey(room_info, on_delete=models.CASCADE)
    # 利用者 : 文字列型30桁
    user = models.CharField(max_length=30)
    # 開始日時 : DATETIME型
    start_date_time = models.DateTimeField(default=timezone.now)
    # 終了日時 : DATETIME型
    end_date_time = models.DateTimeField(default=timezone.now)
    # 削除フラグ : INTEGER型
    del_flg = models.IntegerField()

