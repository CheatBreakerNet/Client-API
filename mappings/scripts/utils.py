import os
import json
from PIL import Image as image

MAJOR_ALL = {
    "1.7.*": ["1.7.10", "1.7"],
    "1.8.*": ["1.8.9", "1.8"]
}


def get_all_servers(servers_dir, inactive_file, include_inactive=True):
    servers = []

    # Open inactive.json
    inactive = []
    with open(inactive_file) as inactive_f:
        inactive = json.load(inactive_f)

    # Looping over each server folder
    for root, _dirs, _files in os.walk(servers_dir):
        server_id = root.split(os.path.sep)[-1]
        if not server_id or server_id == servers_dir:
            continue

        # Open metadata.json
        with open(f"{servers_dir}/{server_id}/metadata.json") as server_file:
            server = json.load(server_file)

        # Modify versions
        if "minecraftVersions" in server:
            server["minecraftVersions"] = get_all_versions(server["minecraftVersions"])

        # Enrich server data
        if "id" not in server:
            print(f"Skipping {server_id} as it's missing 'id'")
            continue
        server["inactive"] = server["id"] in inactive

        if not include_inactive and server["inactive"]:
            continue

        # Add to list
        servers.append(server)

    # Sort A-Z
    servers.sort(key=lambda x: x["id"])

    return servers


def get_all_versions(versions):
    to_return = []

    for version in versions:
        if version in MAJOR_ALL:
            to_return.extend(MAJOR_ALL[version])
        else:
            to_return.append(version)

    return to_return


'''
Validate that server icon meets the following requirements:
  * exists in logos folder
  * is a PNG
  * is 64x64
'''
def validate_icon(path, server_name) -> list:
    # Check image exists

    if not os.path.isfile(path):
        return [
            f'{server_name}\'s server icon does not exist... Please ensure the file name matches the server ID and is a PNG.']

    errors = []
    icon_image = image.open(path)

    # Check image format is a PNG
    if icon_image.format != 'PNG':
        errors.append(
            f'{server_name}\'s server icon is not a PNG (currently {icon_image.format})... Please ensure the image meets the requirements before proceeding.')

    # Check image dimensions are 64x64
    if icon_image.width != 64 or icon_image.height != 64:
        errors.append(
            f'{server_name}\'s server icon resolution is not 64x64... Please ensure the image meets the requirements before proceeding.')

    return errors


'''
Validate that server logo meets the following requirements:
  * exists in logos folder
  * is a PNG
  * is 108x108
'''
def validate_logo(path, server_name) -> list:
    # Check image exists

    if not os.path.isfile(path):
        return [
            f'{server_name}\'s server logo does not exist... Please ensure the file name matches the server ID and is a PNG.']

    errors = []
    logo_image = image.open(path)

    # Check image format is a PNG
    if logo_image.format != 'PNG':
        errors.append(
            f'{server_name}\'s server logo is not a PNG (currently {logo_image.format})... Please ensure the image meets the requirements before proceeding.')

    # Check image dimensions are 108x108
    if logo_image.width != 108 or logo_image.height != 108:
        errors.append(
            f'{server_name}\'s server logo resolution is not 108x108... Please ensure the image meets the requirements before proceeding.')

    return errors

'''
Validate that server Discord logo meets the following requirements:
  * exists in logos folder
  * is a PNG
  * is 512x512 or more (up to 1024x1024)
'''
def validate_discord_logo(path, server_name) -> list:
    # Check image exists

    if not os.path.isfile(path):
        return [
            f'{server_name}\'s server Discord logo does not exist... Please ensure the file name matches the server ID and is a PNG.']

    errors = []
    logo_image = image.open(path)

    # Check image format is a PNG
    if logo_image.format != 'PNG':
        errors.append(
            f'{server_name}\'s server Discord logo is not a PNG (currently {logo_image.format})... Please ensure the image meets the requirements before proceeding.')

    # Check image dimensions are a 1:1 ratio
    if logo_image.width != logo_image.height:
        errors.append(
            f'{server_name}\'s server Discord logo does not have a 1:1 aspect ratio... Please ensure the image meets the requirements before proceeding.')

    # Check image dimensions are 512x512 or more (up to 1024x1024)
    if not (512 <= logo_image.width <= 1024) or not (512 <= logo_image.height <= 1024):
        errors.append(
            f'{server_name}\'s server Discord logo resolution is not 512x512 or more (up to 1024x1024)... Please ensure the image meets the requirements before proceeding.')

    return errors


'''
Validate that server primary background meets the following requirements:
  * is a PNG
  * is 774x363 or 16:9
'''
def validate_primary_background(path, server_name) -> list:
    # Check image exits - silently skip if not (as it is not yet a requirement)
    if not os.path.isfile(path):
        print(f'No primary background found for {server_name}... skipping.')
        return []

    errors = []
    primary_background_image = image.open(path)

    # Check image format is a PNG
    if primary_background_image.format != 'PNG':
        errors.append(
            f'{server_name}\'s server primary background is not a PNG (currently {primary_background_image.format})... Please ensure the image meets the requirements before proceeding.')

    aspect_ratio = primary_background_image.width / primary_background_image.height
    # Check image dimensions are 774x363 or if the aspect ratio is 16:9
    if (abs(aspect_ratio - (16 / 9)) > 0.01):
        if (primary_background_image.width != 774 or primary_background_image.height != 363):
            errors.append(
                f'{server_name}\'s server primary background resolution is not 774x363 or 16:9... Please ensure the image meets the requirements before proceeding.')

    return errors


'''
Validate that server secondary background meets the following requirements:
  * is a PNG
  * is 447x172
'''
def validate_secondary_background(path, server_name) -> list:
    # Check image exits - silently skip if not (as it is not yet a requirement)
    if not os.path.isfile(path):
        print(f'No secondary background found for {server_name}... skipping.')
        return []

    errors = []
    secondary_background_image = image.open(path)

    # Check image format is a PNG
    if secondary_background_image.format != 'PNG':
        errors.append(
            f'{server_name}\'s server secondary background is not a PNG (currently {secondary_background_image.format})... Please ensure the image meets the requirements before proceeding.')

    # Check image dimensions are 447x172
    if secondary_background_image.width != 447 or secondary_background_image.height != 172:
        errors.append(
            f'{server_name}\'s server secondary background resolution is not 447x172... Please ensure the image meets the requirements before proceeding.')

    return errors
