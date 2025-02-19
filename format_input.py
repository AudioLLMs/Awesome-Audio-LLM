import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import json
import os
import numpy as np

# Load JSON files from the 'items' folder
model_cards = []
folder_path = 'items'
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        with open(os.path.join(folder_path, filename), 'r') as f:
            model_cards.append(json.load(f))

# Convert the time strings to datetime objects (include months)
times = [datetime.strptime(card["Time"], "%Y-%m") for card in model_cards]
labels = [card["Abbreviation"] for card in model_cards]

# Group model cards by month
grouped_cards = {}
for card, time in zip(model_cards, times):
    month = time.strftime('%Y-%m')
    if month not in grouped_cards:
        grouped_cards[month] = []
    grouped_cards[month].append(card)

# Sort grouped cards by most recent month first
grouped_cards = dict(sorted(grouped_cards.items(), reverse=True))

# Set up the plot
fig, ax = plt.subplots(figsize=(9, len(grouped_cards) * 2))  # Reduced width of the figure

# Plot the timeline with items listed vertically
y_pos = 0
yticks = []
ytick_labels = []
for month, cards in grouped_cards.items():
    for card in cards:
        label = f"**{card['Abbreviation']}**"
        card_type = card.get("Type", "Unknown Type")
        audio_in = "Audio In" if card.get("Audio_Input", "No") == "Yes" else ""
        audio_out = "Audio Out" if card.get("Audio_Output", "No") == "Yes" else ""
        language = "Multilingual" if card.get('Language', 'Unknown') == 'Multilingual' else card.get('Language', 'Unknown')

        # Build formatted text
        formatted_text_parts = [label, f"Type: {card_type}"]
        if audio_in:
            formatted_text_parts.append(audio_in)
        if audio_out:
            formatted_text_parts.append(audio_out)
        if language:
            formatted_text_parts.append(language)
        formatted_text = ", ".join(filter(None, formatted_text_parts))

        # Add text to the plot
        ax.text(1.05, y_pos, formatted_text, ha="left", va="center", fontsize=10, color="black", weight="bold")
        y_pos -= 1

    # Add month label
    yticks.append(y_pos + len(cards) / 2)
    ytick_labels.append(month)
    y_pos -= 1  # Add space between months

# Set the y-axis ticks and labels
ax.set_yticks(yticks)
ax.set_yticklabels(ytick_labels)

# Adjust the plot
ax.get_xaxis().set_visible(False)
ax.set_xlim(0.95, 2.0)
ax.set_ylim(y_pos, 1)
plt.tight_layout()

# Save the plot locally
plt.savefig('model_release_timeline_vertical_listed.png', dpi=300)

# Group cards by category for README generation
categories = {}
for card in model_cards:
    category = card.get("Category", "Uncategorized")
    if category not in categories:
        categories[category] = []
    categories[category].append(card)

# Sort models within each category by time
def sort_by_time(card):
    return datetime.strptime(card["Time"], "%Y-%m")

for category in categories:
    categories[category].sort(key=sort_by_time, reverse=True)

# Generate README.md content
readme_lines = []
readme_lines.append("### 🌟🌟🌟 Find interesting work or want your work to be on-board? Raise an Issue or Pull Requests! :)")
# Contributors
readme_lines.append("## Contributors")
readme_lines.append("We thank the following contributors for their valuable contributions!")
readme_lines.append("[zwenyu](https://github.com/zwenyu), ")
readme_lines.append("[Yuan-ManX](https://github.com/Yuan-ManX), ")
readme_lines.append("[chaoweihuang](https://github.com/chaoweihuang), ")
readme_lines.append("[Liu-Tianchi](https://github.com/Liu-Tianchi), ")
readme_lines.append("[Sakshi113](https://github.com/Sakshi113), ")
readme_lines.append("[hbwu-ntu](https://github.com/hbwu-ntu), ")
readme_lines.append("[potsawee](https://github.com/potsawee), ")
readme_lines.append("[czwxian](https://github.com/czwxian), ")
readme_lines.append("[marianasignal](https://github.com/marianasignal), ")




# ================== Add the Table of Contents ==================
readme_lines.append("## Table of Contents")
for category in categories:
    anchor = category.lower().replace(" ", "-")
    readme_lines.append(f"- [{category}](#{anchor})")
readme_lines.append("")

readme_lines.append('<img src="model_release_timeline_vertical_listed.png" alt="Timeline Visualization" width="600">')  # Embed smaller image
readme_lines.append("")

# Add a list of abbreviations with links
readme_lines.append("### Abbreviations with Links")
model_cards.sort(key=lambda card: datetime.strptime(card["Time"], "%Y-%m"), reverse=True)

for card in model_cards:
    abbreviation = card["Abbreviation"]
    paper_link = card.get("Paper_Link", "")
    hf_link = card.get("HF_Link", "")
    demo_link = card.get("Demo_Link", "")
    github_link = card.get("GitHub_Link", "")
    other_link = card.get("Other_Link", "")

    # Create a link (default to the paper link, then other available links)
    link = paper_link or hf_link or demo_link or github_link or other_link
    if link:
        readme_lines.append(f"- [{abbreviation}]({link})")
    else:
        readme_lines.append(f"- {abbreviation} (No link available)")

readme_lines.append("")  # Add spacing before categories

for category, cards in categories.items():
    readme_lines.append(f"## {category}\n")
    for card in cards:
        abbreviation = card["Abbreviation"]
        title = card.get("Title", "No title available")
        affiliation = card.get("Affiliation", "Unknown affiliation")
        author = card.get("Author", "Unknown authors")
        card_type = card.get("Type", "Unknown Type")
        paper_link = card.get("Paper_Link", "")
        hf_link = card.get("HF_Link", "")
        demo_link = card.get("Demo_Link", "")
        github_link = card.get("GitHub_Link", "")
        other_link = card.get("Other_Link", "")

        links = []
        if paper_link:
            links.append(f"[Paper]({paper_link})")
        if hf_link:
            links.append(f"[Hugging Face Model]({hf_link})")
        if demo_link:
            links.append(f"[Demo]({demo_link})")
        if other_link:
            links.append(f"[Other Link]({other_link})")

        github_shield = f"[![GitHub stars](https://img.shields.io/github/stars/{'/'.join(github_link.split('/')[-2:])}?style=social)]({github_link})" if github_link else ""

        readme_lines.append(f"- `【{card['Time']}】-【{abbreviation}】-【{affiliation}】-【Type: {card_type}】`")
        readme_lines.append(f"  - **{title}**")
        readme_lines.append(f"  - **Author(s):** {author}")
        if github_shield:
            readme_lines.append(f"  - {github_shield}")
        if links:
            readme_lines.append(f"  - {' / '.join(links)}")
        readme_lines.append("")

# Write to README.md
with open("README.md", "w") as readme_file:
    readme_file.write("\n".join(readme_lines))

# Update with contributors
readme_lines.append("## Contributors")
readme_lines.append("We thank the following contributors for their valuable contributions!")
readme_lines.append("")
readme_lines.append("<!-- Contributors list -->")

readme_lines.append("<!-- Contributors list -->")



print("README.md has been generated.")
