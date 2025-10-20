# Epidemic Simulation with SIR Model

This project simulates the spread of an epidemic using the Susceptible – Infectious – Recovered (SIR) model. The program implements an agent-based model to visualize the epidemic's progression and evaluate different intervention strategies. Users can explore various approaches for managing the epidemic by adjusting parameters like the infection rate, recovery probability, and population size.

## Features
**SIR Model**: The simulation categorizes the population into three groups: Susceptible (S), Infectious (I), and Recovered (R). 
**Intervention Strategies**: Users can test three strategies to control the epidemic:
  1. **Reduce the infection rate** (e.g., social distancing): This strategy slows the spread of the disease by reducing the rate of contact between susceptible and infectious individuals. While it decreases the peak number of infectious people, the epidemic lasts longer.
  2. **Increase the recovery rate** (e.g., improved healthcare): This strategy accelerates the recovery of infectious individuals, shortening the duration of the epidemic. However, it has a less dramatic impact on the number of infections compared to the infection rate reduction strategy.
  3. **Reduce the susceptible population** (e.g., vaccination): By lowering the number of susceptible individuals, this strategy prevents a portion of the population from being exposed to the disease. This can reduce the overall number of infections but may lead to the epidemic starting earlier or having an earlier peak, especially if the susceptible population is significantly reduced.

**Visualization**: Two dynamic graphs are generated:
  1. Population composition over time (Susceptible, Infectious, Recovered)
  2. Percentage of infectious individuals over time
**Interactive Interface**: The program includes a graphical user interface (GUI) to input parameters and display results.

## Walkthrough
For a demonstration of the program's functionality, watch the walkthrough video: [walkthrough.mp4](https://drive.google.com/file/d/1r5y9Sr5Y3CQkJZHfhDmnZnzl3HWlmt2F/view?usp=sharing)

In the walkthrough, the user tests a population of 100,000 people with a contact rate of 0.3 and a recovery rate of 0.1. After simulating the epidemic for 150 days, the user tests different strategies:

1. **Reduce the contact rate** (Strategy 1): 
   **Impact**: The number of infections decreases, with the peak of infectious individuals significantly lower than the status quo. However, the epidemic lasts longer due to the slower spread of the disease.
   
2. **Increase the recovery rate** (Strategy 2):
   **Impact**: The epidemic duration is shortened as people recover faster. There is a slight reduction in the number of infections, but the overall changes are less pronounced than with Strategy 1.

3. **Reduce the susceptible population** (Strategy 3):
   **Impact**: The total number of infections decreases, but the epidemic begins earlier and peaks sooner. When the susceptible population is reduced modestly, the changes are negligible, but larger reductions can significantly alter the epidemic timeline.

The walkthrough illustrates how these strategies affect the spread of the disease and provides insights into which interventions may be most effective.

## Getting Started

1. Clone the repository

   ```bash
   git clone https://github.com/mktran28/SIR-Epidemiological-Simulator-2.0.0.git
   cd SIR-Epidemiological-Simulator-2.0.0
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   # Activate it:
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations

   ```bash
   python manage.py migrate
   ```

5. Run the development server

   ```bash
   python manage.py runserver
   ```

6. Access the web app

   Open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

   Use the form to input simulation parameters and explore the model.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore, modify, and contribute! If you find any bugs or have suggestions for improvements, open an issue or submit a pull request.