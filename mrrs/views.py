import calendar
import datetime
import dateutil.parser
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from .models import room_info, room_reservation
from . import forms


def mrrs(request):

    display = {
        "test": "test",
    }

    return render(request, "resurv.html", display)


def room(request):

    # リクエストがPOST形式の場合 データーベースに会議室予約システムの情報を登録する.
    if request.method == "POST":
        # 会議室ID
        room_id = request.POST.get("room_id")
        # 利用者
        room_name = request.POST.get("room_name")
        # リクエストパラメーターをデーターモデルに当て込みます.
        data_object = room_info(room_id=room_id, room_name=room_name, del_flg=0,)
        # データーを登録する.
        data_object.save()

    # データーモデルからデーターを取得する.
    room_data = room_info.objects.all()
    # フォームオブジェクトを取得する.
    form = forms.reserv_room_info(request.GET or None)
    display = {
        "form": form,
        "room_data": room_data,
    }

    return render(request, "room.html", display)
