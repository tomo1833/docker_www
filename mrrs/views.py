from django.http.response import HttpResponse
from django.shortcuts import render
from . import models
from . import forms

def mrrs(request):
    """
    会議室予約システム画面の関数
    """
    # リクエストがPOST形式の場合 データーベースに会議室予約システムの情報を登録する.
    if request.method == "POST":
        # 予約ID
        reserv_id = request.POST.get('reserv_id')
        # 会議室ID
        room_id = request.POST.get('room_id')
        # 利用者
        reserv_name = request.POST.get('reserv_name')
        # 開始日時
        start_date_time = request.POST.get('start_date_time')
        # 終了日時
        end_date_time = request.POST.get('end_date_time')  

        # リクエストパラメーターをデーターモデルに当て込みます.
        data_object = models.room_reservation(
            id=reserv_id, 
            room_id=models.room_info.objects.get(room_id=room_id) , 
            user=reserv_name, 
            start_date_time=start_date_time, 
            end_date_time=end_date_time, 
            del_flg=0)
        # データーを登録する.
        data_object.save()

    # データーモデルからデーターを取得する.
    reserv_data = models.room_info.objects.select_related('room_reservation').values('room_reservation__id','room_info__room_id', 'room_reserv__name', 'room_reserv__start_date_time', 'room_reserv__end_date_time')
    
    # フォームオブジェクトを取得する.
    form = forms.reserv_room(request.GET or None)
    # テンプレートに渡す値を設定する
    display = {
        'form': form,
        'reserv_data' : reserv_data,
    }

    return render(request, 'resurv.html', display)

def room(request):

    # リクエストがPOST形式の場合 データーベースに会議室予約システムの情報を登録する.
    if request.method == "POST":

        # 会議室ID
        room_id = request.POST.get('room_id')
        # 利用者
        room_name = request.POST.get('room_name') 

        # リクエストパラメーターをデーターモデルに当て込みます.
        data_object = models.room_info(
            room_id=room_id, 
            room_name=room_name, 
            del_flg=0)
        # データーを登録する.
        data_object.save()

    # データーモデルからデーターを取得する.
    room_data = models.room_info.objects.all()
    # フォームオブジェクトを取得する.
    form = forms.reserv_room_info(request.GET or None)
    display = {
        'form': form,
        'room_data' : room_data,
    }
    return render(request, 'room.html', display)
