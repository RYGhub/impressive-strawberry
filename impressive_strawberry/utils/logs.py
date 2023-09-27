import logging
import coloredlogs

this_log = logging.getLogger(__name__)


def install_general_log_handlers():
    main_logger: logging.Logger = logging.getLogger("__main__")

    interesting_loggers: list[logging.Logger] = [
        main_logger,
        logging.getLogger("impressive_strawberry"),
    ]

    this_log.debug("Installing console handlers...")
    for logger in interesting_loggers:
        coloredlogs.install(
            logger=logger,
            level="DEBUG" if __debug__ else "INFO",
            fmt="{asctime} | {name} | {levelname} | {message}",
            style="{",
            level_styles=dict(
                debug=dict(color="white"),
                info=dict(color="cyan"),
                warning=dict(color="yellow", bold=True),
                error=dict(color="red", bold=True),
                critical=dict(color="black", background="red", bold=True),
            ),
            field_styles=dict(
                asctime=dict(color='magenta'),
                levelname=dict(color='blue', bold=True),
                name=dict(color='blue'),
            ),
            isatty=True,
        )
        this_log.debug("Installed console log handler on: %s", logger)


__all__ = (
    "install_general_log_handlers",
)
