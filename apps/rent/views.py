from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def create_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spotify/authors_list_2.html')
        else:
            return render(request, 'about.html', {'form': form})
    else:
        form = ProposalForm
        return render(request, 'about.html', {'form': form})