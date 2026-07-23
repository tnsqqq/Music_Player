import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

console = Console()


def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)
    if not os.path.exists(file_path):
        console.print("[bold red]File not found[/bold red]")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    console.print(
        Panel(
            f"[bold cyan]{song_name}[/bold cyan]",
            title="🎵 Now Playing",
            border_style="green",
            box=box.ROUNDED,
        )
    )
    console.print(
        "[bold]Commands:[/bold] [yellow]P[/yellow]ause  "
        "[yellow]R[/yellow]esume  [yellow]S[/yellow]top\n"
    )

    while True:
        command = Prompt.ask("[bold magenta]>[/bold magenta]").upper()
        if command == "P":
            pygame.mixer.music.pause()
            console.print("[yellow]⏸  Paused[/yellow]")
        elif command == "R":
            pygame.mixer.music.unpause()
            console.print("[green]▶  Resumed[/green]")
        elif command == "S":
            pygame.mixer.music.stop()
            console.print("[red]⏹  Stopped[/red]")
            return
        else:
            console.print("[bold red]Invalid Command![/bold red]")


def show_song_list(mp3_files):
    table = Table(title="🎧 My Song List", box=box.SIMPLE_HEAVY, header_style="bold cyan")
    table.add_column("#", justify="right", style="yellow")
    table.add_column("Song", style="white")

    for index, song in enumerate(mp3_files, start=1):
        table.add_row(str(index), song)

    console.print(table)


def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        console.print(f"[bold red]Audio initialization failed![/bold red] {e}")
        return

    folder = "Music"
    if not os.path.isdir(folder):
        console.print(f"[bold red]Folder '{folder}' not found[/bold red]")
        return

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    if not mp3_files:
        console.print("[bold red]No .mp3 files found![/bold red]")
        return

    while True:
        console.rule("[bold blue]♫ MP3 PLAYER ♫[/bold blue]")
        show_song_list(mp3_files)

        choice_input = Prompt.ask(
            "\n[bold]Enter the song #[/bold] to play (or [yellow]Q[/yellow] to quit)"
        )

        if choice_input.upper() == "Q":
            console.print("[bold cyan]Bye![/bold cyan] 👋")
            break

        if not choice_input.isdigit():
            console.print("[bold red]Enter a valid number[/bold red]")
            continue

        choice = int(choice_input) - 1
        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            console.print("[bold red]Invalid choice![/bold red]")


if __name__ == "__main__":
    main()