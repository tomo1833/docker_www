import calendar
import datetime
from django.shortcuts import render
from .models import room_info, room_reservation
from . import forms


def mrrs(request):
    """
    会議室予約システム画面の関数
    """
    # 月曜日から始まるカレンダー
    cal = calendar.Calendar(0)
    today = datetime.date.today()
    month_days = cal.monthdatescalendar(today.year, today.month)

    # リクエストがPOST形式の場合 データーベースに会議室予約システムの情報を登録する.
    if request.method == "POST":
        # 予約ID
        reserv_id = request.POST.get("reserv_id")
        # 会議室ID
        room_id = request.POST.get("room_id")
        # 利用者
        reserv_name = request.POST.get("reserv_name")
        # 開始日時
        start_date_time = request.POST.get("start_date_time")
        # 終了日時
        end_date_time = request.POST.get("end_date_time")

        if "登 録" in request.POST.get("action"):
            # リクエストパラメーターをデーターモデルに当て込みます.
            data_object = room_reservation(
                id=reserv_id,
                room_id=room_info.objects.get(room_id=room_id),
                user=reserv_name,
                start_date_time=start_date_time,
                end_date_time=end_date_time,
                del_flg=0,
            )
            # データーを登録する.
            data_object.save()

        if "削 除" in request.POST.get("action"):
            # リクエストパラメーターをデーターモデルに当て込みます.
            data_object = room_reservation(
                id=reserv_id,
                room_id=room_info.objects.get(room_id=room_id),
                user=reserv_name,
                start_date_time=start_date_time,
                end_date_time=end_date_time,
                del_flg=0,
            )
            # データーを削除する.
            data_object.delete()

        if "更 新" in request.POST.get("action"):
            # リクエストパラメーターをデーターモデルに当て込みます.
            data_object = room_reservation(
                id=reserv_id,
                room_id=room_info.objects.get(room_id=room_id),
                user=reserv_name,
                start_date_time=start_date_time,
                end_date_time=end_date_time,
                del_flg=1,
            )
            # データーを更新する.
            data_object.save()

    # データーモデルからデーターを取得する.
    roon_data = room_info.objects.all()
    reserv_data = room_reservation.objects.filter(
        start_date_time__year=today.year,
        start_date_time__month=today.month,
        start_date_time__day=today.day,
    )

    # フォームオブジェクトを取得する.
    form = forms.reserv_room(request.GET or None)
    # テンプレートに渡す値を設定する
    display = {
        "form": form,
        "roon_data": roon_data,
        "reserv_data": reserv_data,
        "month_days_text": "{0:%Y年%m月}".format(today),
        "month_days": month_days,
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
