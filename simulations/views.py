from django.shortcuts import render, redirect
from .forms import SimulationForm
import main

def index(request):
    # Initial page with form
    form = SimulationForm()
    return render(request, 'index.html', {'form': form})

def result(request):
    if request.method == 'POST':
        # Run baseline
        if 'baseline_submitted' in request.POST:
            form = SimulationForm(request.POST)
            if form.is_valid():
                num_days = form.cleaned_data['num_days']
                population = form.cleaned_data['population']
                recover_prob = form.cleaned_data['recover_prob']
                contact_rate = form.cleaned_data['contact_rate']

                main.normalGraph(num_days, population, recover_prob, contact_rate)

                # Store baseline in session
                request.session['baseline'] = {
                    'num_days': num_days,
                    'population': population,
                    'recover_prob': recover_prob,
                    'contact_rate': contact_rate,
                }

                return render(request, 'result.html', {
                    'img_path': 'normal_graph.png',
                    'show_strategy_options': True
                })
            else:
                return render(request, 'index.html', {'form': form})

        # Run the selected strategy
        elif 'strategy' in request.POST:
            baseline = request.session.get('baseline')
            if not baseline:
                return redirect('index')

            strategy = request.POST.get('strategy')
            img_path = None
            error = None

            # Handle each strategy
            if strategy == 'strategy1':
                new_val = request.POST.get('new_contactRate')
                if new_val:
                    try:
                        new_contact_rate = float(new_val)
                        if 0 < new_contact_rate < 1:
                            main.strategy1Graph(
                                baseline['num_days'], baseline['population'],
                                baseline['recover_prob'], baseline['contact_rate'],
                                new_contact_rate
                            )
                            img_path = 'strategy1_graph.png'
                        else:
                            error = 'Contact rate must be between 0 and 1.'
                    except ValueError:
                        error = 'Please enter a valid number for the contact rate.'
                else:
                    error = 'Please enter a new contact rate.'

            elif strategy == 'strategy2':  # Recovery probability change
                new_val = request.POST.get('new_recoverProb')
                if new_val:
                    try:
                        new_recover_prob = float(new_val)
                        if 0 < new_recover_prob < 1:
                            main.strategy2Graph(
                                baseline['num_days'], baseline['population'],
                                baseline['recover_prob'], baseline['contact_rate'],
                                new_recover_prob
                            )
                            img_path = 'strategy2_graph.png'
                        else:
                            error = 'Recovery probability must be between 0 and 1.'
                    except ValueError:
                        error = 'Please enter a valid number for the recovery probability.'
                else:
                    error = 'Please enter a new recovery probability.'

            elif strategy == 'strategy3':  # Population size change
                new_val = request.POST.get('new_numPeople')
                if new_val:
                    try:
                        new_population = int(new_val)
                        if new_population > 0:
                            main.strategy3Graph(
                                baseline['num_days'], baseline['population'],
                                baseline['recover_prob'], baseline['contact_rate'],
                                new_population
                            )
                            img_path = 'strategy3_graph.png'
                        else:
                            error = 'Population size must be a positive integer.'
                    except ValueError:
                        error = 'Please enter a valid number for the population size.'
                else:
                    error = 'Please enter a new susceptible population size.'

            # Return with error message or show the graph for the selected strategy
            if error:
                return render(request, 'result.html', {
                    'img_path': 'normal_graph.png',
                    'show_strategy_options': True,
                    'selected_strategy': strategy,
                    'error': error,
                })

            return render(request, 'result.html', {
                'img_path': img_path,
                'show_strategy_options': True,
                'try_another_strategy': True,
            })

    # Handling GET request
    elif request.method == 'GET':
        baseline = request.session.get('baseline')
        if baseline:
            # If baseline is set, show the graph
            main.normalGraph(baseline['num_days'], baseline['population'], baseline['recover_prob'], baseline['contact_rate'])
            return render(request, 'result.html', {
                'img_path': 'normal_graph.png',
                'show_strategy_options': True,
            })
        else:
            # Redirect to index if baseline data is missing
            return redirect('index')

    return redirect('index')