from django import forms
from django.core.exceptions import ValidationError
from . import models


class reserv_room(forms.Form):
    """
    reserv_roomのフォーム.

    """

    # 予約ID
    reserv_id = forms.CharField(
        label="ID",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
    # 会議室ID
    room_id = forms.ModelChoiceField(
        models.room_info.objects, label="会議室名", required=True,
    )
    # 利用者
    reserv_name = forms.CharField(
        label="利用者",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
    # 開始日時
    start_date_time = forms.SplitDateTimeField(label="開始日時", required=True)

    # 終了日時
    end_date_time = forms.SplitDateTimeField(label="終了日時", required=True)

    def clean(self):
        all_clean_data = super().clean()
        start_date_time = all_clean_data["start_date_time"]
        end_date_time = all_clean_data["end_date_time"]

        if start_date_time >= end_date_time:
            raise forms.ValidationError("終了日時は開始日時より後を選択して下さい。")
        return all_clean_data


class reserv_room_info(forms.Form):
    """
    reserv_room_infoのフォーム.

    """

    # 会議室ID
    room_id = forms.CharField(
        label="会議室ID",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
    # 会議室名
    room_name = forms.CharField(
        label="会議室名",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
