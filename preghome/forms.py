from django import forms
from  .models import BookNurse

NURSE_PACKAGES = [
	('POSTNATALCARE','PostNatalCare'),
	('PALIATIVECARE','PaliativeCare'),
	('BEDSIDENURSE', 'BedSideNurse')
]

class BookNurseForm(forms.ModelForm):
	package = forms.CharField(label="Choose Package", widget=forms.Select(choices=NURSE_PACKAGES))

	class Meta:
		model = BookNurse
		fields = ['contact','location','no_days']