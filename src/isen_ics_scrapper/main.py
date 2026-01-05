import requests
from ics import Calendar
from collections import defaultdict
import typer
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from datetime import timedelta

app = typer.Typer()
console = Console()

def download_ics(url: str) -> str:
    """Télécharge le fichier ICS depuis l'URL donnée."""
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'
    return response.text

def parse_ics_and_count_hours(ics_content: str) -> dict:
    """Parse le contenu ICS et compte les heures par cours."""
    c = Calendar(ics_content)
    course_hours = defaultdict(float)

    for event in c.events:
        # On suppose que le nom du cours est dans le titre (summary)
        # On nettoie parfois le titre si nécessaire, ici on prend le titre brut
        course_name = event.name.strip() if event.name else "Inconnu"
        
        duration = event.duration
        # duration est un timedelta
        hours = duration.total_seconds() / 3600
        course_hours[course_name] += hours

    return course_hours

@app.command()
def main(student_id: str):
    """
    Télécharge l'emploi du temps ISEN pour l'ID étudiant donné et affiche le total des heures par matière.
    """
    url = f"https://web.isen-ouest.fr/ICS/{student_id}.ics"
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=f"Téléchargement de l'emploi du temps pour {student_id}...", total=None)
        try:
            ics_content = download_ics(url)
        except requests.RequestException as e:
            console.print(f"[bold red]Erreur lors du téléchargement :[/bold red] {e}")
            raise typer.Exit(code=1)

    course_hours = parse_ics_and_count_hours(ics_content)

    # Création du tableau Rich
    table = Table(title=f"Répartition des heures de cours (ID: {student_id})")

    table.add_column("Matière", style="cyan", no_wrap=False)
    table.add_column("Heures Totales", justify="right", style="magenta")

    # Tri des cours par nombre d'heures décroissant
    sorted_courses = sorted(course_hours.items(), key=lambda item: item[1], reverse=True)

    total_hours = 0
    for course, hours in sorted_courses:
        table.add_row(course, f"{hours:.2f} h")
        total_hours += hours

    table.add_section()
    table.add_row("TOTAL", f"[bold]{total_hours:.2f} h[/bold]")

    console.print(table)

if __name__ == "__main__":
    app()
