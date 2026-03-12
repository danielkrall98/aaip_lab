import pandas as pd
import plotly.graph_objects as go

url = "https://raw.githubusercontent.com/ADSLab-Salzburg/DataAnalysiswithPython/main/data/titanic.csv"
df = pd.read_csv(url)

df = df.dropna(subset=['Embarked', 'Survived'])

sankey_data = (df.groupby(['Embarked', 'Survived']).size().reset_index(name='Count'))

# Node labels
node_labels = ['C', 'Q', 'S', 'Did Not Survive', 'Survived']

# Dictionary that maps each node label to an index
node_map = {label: i for i, label in enumerate(node_labels)}

# Dictionary to map survival
survival_map = {
    1: node_map['Survived'],        # Map 1 to the "Survived" node
    0: node_map['Did Not Survive']  # Map 0 to the "Did Not Survive" node
}

# Source, Targets, Value for Sankey Diagram
sources = sankey_data['Embarked'].map(node_map)
targets = sankey_data['Survived'].map(survival_map)
values = sankey_data['Count']

# Create Sankey Diagram
fig = go.Figure(go.Sankey(
    node=dict(pad=None, thickness=30,
    line=dict(color="black", width=0.5),
    label=node_labels),
    link=dict(source=sources, target=targets, value=values)
))

fig.update_layout(
    title_text="Titanic Passengers by Embarking Location and Survival Status",
    font_size=12
)

fig.show()