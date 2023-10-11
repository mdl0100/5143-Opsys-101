import time
from rich import print
from rich.table import Table
from rich.box import SIMPLE
from sqliteCRUD import SQLiteCrud
from random import randint

class FileSys(SQLiteCrud):
    """
        This class represents a filesystem
        and uses the SQLiteCrud class to
        perform CRUD operations on the
        filesystem database.
    """
    def __init__(self, database, table):
        super().__init__(database, table)
        self.database = database
        self.table = table
        self.current_directory_name = "/"
        self.current_directory_id = 1


    def display_ls(self, long=False, hidden=False, readable=False):
        """
            Displays the contents of the current directory

            Parameters:
                long (bool): Display the long format
                hidden (bool): Display hidden files
                readable (bool): Display file size in human readable format
        """
        table = Table(show_header=True, header_style="bold blue", box=SIMPLE)
        data  = self.read_data(self.table, condition_column="pid", condition_value=self.current_directory_id, order_by="filename")
        if not long:
            table.add_column("Filename")
            for row in data:
                table.add_row(row["filename"])
        else:
            table.add_column("Permissions", style="dim", width=12)
            table.add_column("Owner", justify="center")
            table.add_column("Owner_Group", justify="center")
            table.add_column("File_size", justify="right")
            table.add_column("Last Modified", justify="right")
            table.add_column("Filename")
            if readable:
                for row in data:
                    row['file_size'] = convert_size(row['file_size'])
            
            if hidden:
                try:
                    dot = self.read_data(self.table, condition_column="id", condition_value=self.current_directory_id)
                    table.add_row(
                        dot[0]["permissions"],
                        dot[0]["owner"],
                        dot[0]["group_name"],
                        str(dot[0]["file_size"]) if not readable else convert_size(dot[0]["file_size"]),
                        dot[0]["modification_time"],
                        "."
                    )
                    double_dot = self.read_data(self.table, condition_column="id", condition_value=dot[0]["pid"])
                    table.add_row(
                        double_dot[0]["permissions"],
                        double_dot[0]["owner"],
                        double_dot[0]["group_name"],
                        str(double_dot[0]["file_size"]) if not readable else convert_size(double_dot[0]["file_size"]),
                        double_dot[0]["modification_time"],
                        ".."
                    )
                except:
                    pass
                for row in data:
                    if row['hidden']:
                        table.add_row(
                            row["permissions"],
                            row["owner"],
                            row["group_name"],
                            str(row["file_size"]),
                            row["modification_time"],
                            row["filename"]
                        )
            for row in data:
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
        time.sleep(5)

    def mkdir(self, directory, folder_name="New Folder"):
        """
            Creates a new folder in the specified directory

            Parameters:
                directory (str): The current directory
                folder_name (str): The name of the new folder
        """
        current_directory = self.read_data(self.table, condition_column="pid", condition_value=self.current_directory_id)
        folder_exists = True if  self.read_data(self.table, condition_column="filename", condition_value=folder_name) else False
        if folder_exists:
            print("Folder already exists.")
            return
        else:
            data = {
                "pid": self.current_directory_id,
                "filename": folder_name,
                "permissions": "drwxr-xr-x",
                "owner": "user_M",
                "group_name": "group_M",
                "file_size": randint(100, 1000000),
                "modification_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "hidden": 0, 
                "file_type": "folder",
                "content": None
            }
            inserted_data = []
            for col in self.columns:
                if col == "id":
                    continue
                inserted_data.append(data[col])
            self.insert_data(self.table, tuple(inserted_data), tuple(self.columns[1:]))
            print(f"Folder '{folder_name}' created.")
            time.sleep(1)

def display_pwd(directory):
    print(f"[bold cyan]Current Directory:[/bold cyan] [green]{directory}[/green]")
    time.sleep(1)

def convert_size(size):
    if size:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                break
            size /= 1024.0
        return f"{size:.1f} {unit}"
    return size


if __name__ == "__main__":
    # Create the database
    database = "filesystem.sqlite"
    table = "filesystem"    
    db = FileSys("filesystem.sqlite", table)

    # Create the filesystem table

    # check = db.read_data("filesystem", order_by="filename")
    # print(check)
    
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

