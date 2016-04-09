from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

# def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#         self.fields['contact_name'].label = "Tu nombre:"
#         self.fields['contact_email'].label = "Tu correo:"
#         self.fields['content'].label = 
#             "¿Qué nos quieres decir?"