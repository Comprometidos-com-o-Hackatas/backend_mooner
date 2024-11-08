from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.django_populate.infra.populate.management.commands._users import Populate_Users
from core.django_populate.infra.populate.management.commands._genres import Populate_genre
from core.django_populate.infra.populate.management.commands._artist import Artist_Populate
from core.django_populate.infra.populate.management.commands._documents import populate_documents
from core.django_populate.infra.populate.management.commands._images import populate_images
from core.django_populate.infra.populate.management.commands._songs import Populate_songs

class Command(BaseCommand):
    """
     Populates the database with the minimum information for the system to work.
    If the database is not empty, some data will not be populated.

    Raises:
        CommandError: If something goes wrong
    """

    help = """
        Populates the database with the minimum information for the system to work.
        If the database is not empty, some data will not be populated.
    """


    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--genre",
            action='store_true',
            help="Insert genre in database"
        )
        parser.add_argument(
            "--users",
            action='store_true',
            help="Insert users in database"
        )
        parser.add_argument(
            "--artists",
            action='store_true',
            help="Insert artists in database"
        )
        parser.add_argument(
            "--documents",
            action="store_true",
            help="Insert documents in database"
        )
        parser.add_argument(
            "--images",
            action="store_true",
            help="Insert all images in database"
        )
        parser.add_argument(
            "--songs",
            action="store_true",
            help="Insert all songs in database"
        )
        parser.add_argument(
            "--all",
            action='store_true',
            help="Insert all itens in database"
        )
    
    def handle(self, *args, **options):
        try:
            if options.get("genre"):
                self.__handle_genre()
            if options.get("users"):
                self.__handle_users()
            if options.get("artists"):
                self.__handle_artist()
            if options.get("documents"):
                self.__handle_documents()
            if options.get("images"):
                self.__handle_images()
            if options.get("songs"):
                self.__handle_songs()
            if options.get("all"):
                self.__handle_all()

            self.stdout.write(
                self.style.SUCCESS(
                    "\n Data successfully populated :D"
                )   
            )

        except CommandError as e:
            raise CommandError("Check if the parameters are correct") from e
    
    def __handle_genre(self) -> None:
        self.stdout.write("Populating genres data in the database...", ending=" ")
        Populate_genre()
        self.stdout.write(self.style.SUCCESS("OK"))
     
    def __handle_songs(self) -> None:
        self.stdout.write("Populating songs data in the database...", ending=" ")
        Populate_songs()
        self.stdout.write(self.style.SUCCESS("OK"))
    
    def __handle_artist(self) -> None:
        self.stdout.write("Populating artist data in the database...", ending=" ")
        Artist_Populate()
        self.stdout.write(self.style.SUCCESS("OK"))
    
    def __handle_users(self) -> None:
        self.stdout.write("Populating users data in the database...", ending=" ")
        Populate_Users()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_documents(self) -> None:
        self.stdout.write("Populating documents data in the database...", ending=" ")
        populate_documents()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_images(self) -> None:
        self.stdout.write("Populating images in the database...", ending=' ')
        populate_images()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self) -> None:
        self.stdout.write("Populating data in the database...", ending=" ")
        Populate_genre()
        Populate_Users()
        Artist_Populate()
        populate_documents()
        populate_images()
        Populate_songs()
        self.stdout.write(self.style.SUCCESS("OK"))
