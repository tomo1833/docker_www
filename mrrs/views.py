from django.http.response import HttpResponse
from django.shortcuts import render
from .models import room_reservation

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

        if '登 録' in request.POST.get('action'): 
            # リクエストパラメーターをデーターモデルに当て込みます.
            data_object = room_reservation(
                id=reserv_id, 
                room_id=room_id, 
                user=reserv_name, 
                start_date_time=start_date_time, 
                end_date_time=end_date_time, 
                del_flg=0)
            # データーを登録する.
            data_object.save()
        
        if '削 除' in request.POST.get('action'): 
            # リクエストパラメーターをデーターモデルに当て込みます.
            data_object = room_reservation(
                id=reserv_id, 
                room_id=room_id, 
                user=reserv_name, 
                start_date_time=start_date_time, 
                end_date_time=end_date_time, 
                del_flg=0)
            # データーを論理削除する.
            data_object.delete()

        if '更 新' in request.POST.get('action'): 
            # リクエストパラメーターをデーターモデルに当て込みます.
            data_object = room_reservation(
                id=reserv_id, 
                room_id=room_id, 
                user=reserv_name, 
                start_date_time=start_date_time, 
                end_date_time=end_date_time, 
                del_flg=1)
            # データーを論理削除する.
            data_object.save()


    # データーモデルからデーターを取得する.
    reserv_data = room_info.objects.filter(room_reservation__room_id__isnull=True)

    # フォームオブジェクトを取得する.
    form = forms.reserv_room(request.GET or None)
    # テンプレートに渡す値を設定する
    display = {
        'form': form,
        'reserv_data' : reserv_data,
    }

    return render(request, 'resurv.html', display)
