# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
import os

import digitalhub as dh
import digitalhub_runtime_hera # noqa: F401
from digitalhub.runtimes.enums import RuntimeEnvVar
from digitalhub.utils.logger.logger import get_logger

logger = get_logger(__file__)


def main():
    """
    Main function. Get run from backend and execute function.
    """

    logger.info("Getting run from backend.")
    run = dh.get_run(
        os.getenv(RuntimeEnvVar.RUN_ID.value),
        os.getenv(RuntimeEnvVar.PROJECT.value),
    )

    logger.info("Executing workflow.")
    run.run()

    logger.info("Done.")


if __name__ == "__main__":
    main()
