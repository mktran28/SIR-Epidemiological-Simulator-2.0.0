from django import forms

class SimulationForm(forms.Form):
    num_days = forms.IntegerField(
        label='Number of Days',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    population = forms.IntegerField(
        label='Population Size',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    recover_prob = forms.FloatField(
        label='Recovery Probability',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    contact_rate = forms.FloatField(
        label='Contact Rate',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )