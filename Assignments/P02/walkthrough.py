import time
from rich import print
from rich.table import Table
from rich.box import SIMPLE
from sqliteCRUD import SQLiteCrud


def display_ls(files, long=False, hidden=False, readable=False):
    table = Table(show_header=True, header_style="bold blue", box=SIMPLE)
    if not long:
        table.add_column("Filename")
        for row in files:
            table.add_row(row["filename"])
    else:
        table.add_column("Permissions", style="dim", width=12)
        table.add_column("Owner", justify="center")
        table.add_column("Owner_Group", justify="center")
        table.add_column("File_size", justify="right")
        table.add_column("Last Modified", justify="right")
        table.add_column("Filename")
        if readable:
            for row in files:
                row['file_size'] = convert_size(row['file_size'])
        
        if hidden:
            for row in files:
                if row['hidden']:
                    table.add_row(
                        row["permissions"],
                        row["owner"],
                        row["group_name"],
                        str(row["file_size"]),
                        row["modification_time"],
                        row["filename"]
                    )
        for row in files:
            if not row['hidden']:
                table.add_row(
                    row["permissions"],
                    row["owner"],
                    row["group_name"],
                    str(row["file_size"]),
                    row["modification_time"],
                    row["filename"]
                )


    print(table)
    time.sleep(10)

def display_pwd(directory):
    print(f"[bold cyan]Current Directory:[/bold cyan] [green]{directory}[/green]")
    time.sleep(1)

def convert_size(size):
    if size:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                break
            size /= 1024.0
        return f"{size:.1f}{unit}"
    return size


if __name__ == "__main__":
    # Create the database
    database = "filesystem.sqlite"
    table = "filesystem"    
    db = SQLiteCrud("filesystem.sqlite", table)

    # Create the filesystem table

    check = db.read_data("filesystem", order_by="filename")
    # print(check)
    
    # Demonstrate the commands
    print("[bold blue]Command:[/bold blue] [green]ls[/green]")
    display_ls(check, long=False)

    print("[bold blue]Command:[/bold blue] [green]ls -l[/green]")
    display_ls(check, long=True)

    print("[bold blue]Command:[/bold blue] [green]ls -la[/green]")
    display_ls(check, long=True, hidden=True)

    print("[bold blue]Command:[/bold blue] [green]ls -lah[/green]")
    display_ls(check, long=True, hidden=True, readable=True)



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

