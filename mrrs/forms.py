from django import forms


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
    room_id = forms.CharField(
        label="会議室ID",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
    # 利用者
    reserv_name = forms.CharField(
        label="利用者",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
    # 開始日時
    start_date_time = forms.CharField(
        label="開始日時",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )
    # 終了日時
    end_date_time = forms.CharField(
        label="終了日時",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"class": "reserve_type_text"}),
    )


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
