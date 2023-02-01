# Server Mappings

## Summary

This is a public mapping of server IPs <-> a pretty display name. This data is used extensively around Offline CheatBreaker, most notably when displaying server names (or "Private Server", if unknown) on the friends list and the Discord RPC. Historically, this mapping was handled internally, and server owners did not have a good way to manage data for their server.

## How do I add/update/remove a server?

Each server in this repository is represented by a folder with an accompanying `metadata.json`, `logo.png`, `icon.png`, `primarybackground.png` and `secondarybackground.png`. Open a [pull request](https://github.com/Offline-CheatBreaker/Client-API/pulls) in this repository whilst following the steps below, and we'll review it as soon as possible. Once merged, Offline CheatBreaker's services will update over the next 5 minutes (depending on when the cache resets). Check out `metadata.example.json` as an example of how to structure your metadata file.

## IP Addresses

The `addresses` array in each server object is actually an array of IP _suffixes_. For example, `"addresses": ["goldenpvp.net", "other.domain"]` will match `goldenpvp.net`, `na.goldenpvp.net`, `play.other.domain`, and so on. The `primaryAddress` field is where you can include the desired subdomain (`na.goldenpvp.net`, `play.goldenpvp.net`) for users to connect to your server on and is required to be resolvable. This primary address will be used to ensure that the server remains online and active.

## Primary Info & Minecraft Versions

We also require your server's primary connection information and allowed client versions. The `primaryAddress` field should be an address **included** in the `addresses` array.

The `minecraftVersions` field must be an array of client versions allowed on your Minecraft server. *(ie. 1.7.10, 1.8.9)*; The `primaryMinecraftVersion` field must be a subversion of a major version included in the `minecraftVersions` array. **The versions you include must be versions that are directly offered in Offline CheatBreaker**, which can be found in the version selector of the Offline CheatBreaker Launcher.

If your server supports all of the subversions within a major version, you can list the version in `minecraftVersions` as `1.7.*`, but you will still need to specify the specific subversion in the `primaryMinecraftVersion` as this is the specific version that the client uses to Launch you into the game for Quick Connecting.

## Logos

In addition to the data that you will need to provide in your `metadata.json`, you will need to upload a `.png` version of your logo (108x108 `logo.png`) and server icon (64x64 `icon.png`) into the same folder. All images are to be _transparent_.

## Backgrounds

Servers are also required to provide background images, you will need to upload a `.png` version of the primary background (774x363 `primarybackground.png`) and a secondary background (447x172 `secondarybackground.png`) into the same folder as your `metadata.json`. Images should represent either the artistic style or the content of the server. Backgrounds should be free of marketing, text, and/or any logos (on the primary background) (that isn't part of a build).

## Regions

In your `metadata.json`, you can define both a `primaryRegion` and `regions` which your server supports. Below is a table of the regions.

| Region Code | Name |
| --- | --- |
| AF | Africa |
| AS | Asia |
| EU | Europe |
| NA | North America |
| OC | Oceania |
| SA | South America |

## Game Types

Game types help identify the style of games that your server will offer to player. The following are games you may include: `PvP`, `PvE`, `HCF`, `Factions`, `Minigames`, `Skyblock`, `Parkour`, `UHC`, `Hardcore`, `Survival`, `Open World`, `Prison`, `Creative`, `Roleplay`, and `Adventure`.

You can add up to 3 unique types on the `gameTypes` field in your `metadata.json`.

## Restrictions

We ask that this repository is only used to store mappings for *public* Minecraft servers. Some server IPs, such as private SMPs, tournament servers, etc. should not be listed in this repository, out of respect for privacy.

Offline CheatBreaker reserves the right to omit any servers.

## Inactive Server Policy

If a server has closed down or has not been joinable for at least 3 months, we will add it to the `inactive.json`. This just flags our internal systems to not include the server in various place, but still retains all of the branding and other metadata you submit.

If you think your server has been added to this list by mistake, please create a new [issue](https://github.com/Offline-CheatBreaker/Client-API/issues).

## Any other questions?

Please create a new [issue](https://github.com/Offline-CheatBreaker/Client-API/issues) for any additional questions.