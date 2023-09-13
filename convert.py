import csv
import json
from pathlib import Path


def get_data(path):
    """read the json data from specified path"""
    return json.loads(path.read_text())


def get_skills(recipe, format="html"):
    """return the skills string"""
    string_skills = []
    for skill, level in recipe["skill"].items():
        string_skills.append(f"{skill} ({level})")
    return ", ".join(string_skills)


def get_components(recipe, format="html"):
    """return the list of components as a string"""
    string_components = []
    for component, count in sorted(recipe["components"].items()):
        string_components.append(f"{count}x {component}")
    return "<br \> ".join(string_components)


def process_section(section_data, format="html"):
    """
    process the sections converting them to a different format.
    There is only one right now.
    """
    section = "<table class='table is-striped'><tr>\n"
    section += "<th>Name</th>"
    section += "<th>Mass</th>"
    section += "<th>Value</th>"
    section += "<th>Required Skill</th>"
    section += "<th>Components</th>\n"
    section += "</tr>\n"

    for key, value in sorted(section_data.items()):
        print(key)
        row = '<tr class="item">'
        row += f'<td class="name string">{key}</td>\n'
        row += f'<td class="mass float">{value["mass"]}</td>\n'
        row += f'<td class="value int">{value["value"]}</td>\n'
        row += f'<td class="skill string">{get_skills(value)}</td>\n'
        row += f'<td class="skill string">{get_components(value)}</td>\n'
        row += "</tr>\n"
        section += row

    section += "</table>\n"
    return section


def make_html(data):
    """convert the data to html tables"""
    page_header = "<html><body>"
    page_header += '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">\n'
    page_footer = "<body></html>"
    page = page_header

    for section_name in data:
        page += f"<h1 class='m-4 is-size-2 has-text-weight-bold'>{section_name}</h1>\n"
        section = process_section(data[section_name])
        page += section

    return page + page_footer


def main():
    path = Path("industrial_workbench_recipes.json")
    data = get_data(path)
    html = make_html(data)
    output_path = Path(path.stem + ".html")
    output_path.write_text(html)


if __name__ == "__main__":
    main()
