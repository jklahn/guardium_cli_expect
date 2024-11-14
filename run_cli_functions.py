from guard_cli import GuardCLI

cli_host = ""
cli_password = ""
cli_session = None


def gen_cli_session():
    global cli_session

    if cli_session:
        cli_session.close()

    try:
        cli_session = GuardCLI(host=cli_host,
                               port=22,
                               username="cli",
                               password=cli_password)
    # cli_session.get_transport().send_ignore()  # Dummy packet to test the connection

    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':    # code to execute if called from command-line

    # makes a CLI session (cli_session) and includes the CLI functions defined in GuardCLI
    gen_cli_session()

    cli_session.get_available_patches_for_install()
