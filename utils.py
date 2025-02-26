import os


def log(msg, verbose):
    if verbose:
        print(msg)


def get_new_filename(filepath):
    try:
        org_filename = os.path.basename(filepath)
        new_filename = f"framed-{org_filename}"
        new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
        return new_filepath
    except Exception:
        return "framed-testimg.jpg"
