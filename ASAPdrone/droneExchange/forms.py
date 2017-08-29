from django import forms
from droneExchange.models import UserFootage, Details, Message


class UserFootageForm(forms.ModelForm):
    class Meta:
        model = UserFootage
        fields = ["link", "description"]


CITIES = [

    ("Białystok"  ,"Białystok"  ),
    ("Bydgoszcz"  ,"Bydgoszcz"  ),
    ("Częstochowa","Częstochowa"),
    ("Gdynia"     ,"Gdynia"     ),
    ("Gdańsk"     ,"Gdańsk"     ),
    ("Łódź"       ,"Łódź"       ),
    ("Katowice"   ,"Katowice"   ),
    ("Kraków"     ,"Kraków"     ),
    ("Lublin"     ,"Lublin"     ),
    ("Opole"      ,"Opole"      ),
    ("Poznań"     ,"Poznań"     ),
    ("Radom"      ,"Radom"      ),
    ("Sosnowiec"  ,"Sosnowiec"  ),
    ("Szczecin"   ,"Szczecin"   ),
    ("Toruń"      ,"Toruń"      ),
    ("Warszawa"   ,"Warszawa"   ),
    ("Wrocław"    ,"Wrocław"    ),

]


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ["about_me", "pricing", "video_type", "cities"]

class EditDetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ["about_me", "pricing", "video_type", "cities"]


class UserSearchForm(forms.Form):
    city = forms.ChoiceField(choices=CITIES)
    maximum_price = forms.IntegerField(initial=1000)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]