from django.contrib.staticfiles.management.commands.runserver import (
    Command as RunserverCommand
)
from django.conf import settings


class Command(RunserverCommand):
    help = "Starts a lightweight Web server for development with remote debugger option."

    default_remote_debug_port = 3000
    default_remote_debug_addr = '0.0.0.0'
    default_remote_debug_pass = 'debug'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.add_argument(
            '--remote-debug', action='store_true', dest='use_remote_debugger',
            help='Tells Django to WAIT a remote debugger to attach.',
        )

    def handle(self, *args, **options):

        self.remote_debug_port = getattr(
            settings, 'REMOTE_DEBUG_PORT', self.default_remote_debug_port)
        self.remote_debug_addr = getattr(
            settings, 'REMOTE_DEBUG_ADDR', self.default_remote_debug_addr)
        self.remote_debug_pass = getattr(
            settings, 'REMOTE_DEBUG_PASS', self.default_remote_debug_pass)

        super(Command, self).handle(*args, **options)

    def inner_run(self, *args, **options):

        if options['use_remote_debugger']:
            # Setup ptvsd
            # TODO: Check if ptvsd is available
            import ptvsd
            ptvsd.enable_attach(
                self.remote_debug_pass,
                address=(self.remote_debug_addr, self.remote_debug_port)
            )

        super(Command, self).inner_run(*args, **options)
