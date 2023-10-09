import time
from rich import print
from rich.table import Table
from rich.box import SIMPLE
from sqliteCRUD import SQLiteCrud

def display_ls(files):
    table = Table(show_header=True, header_style="bold blue", box=SIMPLE)
    table.add_column("Permissions", style="dim", width=12)
    table.add_column("Owner", width=10)
    table.add_column("Owner_Group", width=10)
    table.add_column("Size", justify="right")
    table.add_column("Last Modified", justify="right")
    table.add_column("Filename")


    for filename, (owner, perms, size) in files.items():
        table.add_row(filename, owner, perms, size)
    print(table)
    time.sleep(10)

def display_pwd(directory):
    print(f"[bold cyan]Current Directory:[/bold cyan] [green]{directory}[/green]")
    time.sleep(1)

if __name__ == "__main__":
    # Create the database
    db = SQLiteCrud("filesystem.sqlite")
    table = "filesystem"
    
    check = db.read_data("filesystem")
    print(db.__raw_results(check))
    
    # # Demonstrate the commands
    # print("[bold blue]Command:[/bold blue] [green]ls[/green]")
    # display_ls(table)

    # print("\n[bold blue]Command:[/bold blue] [green]mkdir newfolder[/green]")
    # print("[bold green]Folder 'newfolder' created.[/bold green]")
    # time.sleep(1)

    # print("\n[bold blue]Command:[/bold blue] [green]ls[/green]")
    # display_ls(files_after)

    # print("\n[bold blue]Command:[/bold blue] [green]cd newfolder[/green]")
    # current_directory += "/newfolder"
    # display_pwd(current_directory)

    # print("\n[bold blue]Command:[/bold blue] [green]cp ../file1.txt .[/green]")
    # print("[bold green]File 'file1.txt' copied to current directory.[/bold green]")
    # time.sleep(1)

    # print("\n[bold blue]Command:[/bold blue] [green]rm ../file1.txt ../file2.txt ../file5.txt[/green]")
    # print("[bold green]Files 'file1.txt', 'file2.txt', and 'file5.txt' removed.[/bold green]")
    # time.sleep(1)

    # print("\n[bold blue]Command:[/bold blue] [green]ls[/green]")
    # display_ls(files_after)

    # print("\n[bold blue]Command:[/bold blue] [green]pwd[/green]")
    # display_pwd(current_directory)