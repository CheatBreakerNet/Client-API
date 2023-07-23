# Server Mappings

## Summary

This is a public mapping of server IPs <-> a pretty display name. This data is used extensively around CheatBreaker, most notably when displaying server names (or "Private Server", if unknown) on the friends list and the Discord RPC. Historically, this mapping was handled internally, and server owners did not have a good way to manage data for their server.

## How do I add/update/remove a server?

Each server in this repository is represented by a folder with an accompanying `metadata.json`, `logo.png`, `icon.png`, `primarybackground.png` and `secondarybackground.png`. Open a [pull request](https://github.com/CheatBreakerNet/Client-API/pulls) in this repository whilst following the steps below, and we'll review it as soon as possible. Once merged, CheatBreaker's services will update over the next 5 minutes (depending on when the cache resets). Check out `metadata.example.json` as an example of how to structure your metadata file.

**Note: Do not modify any other repository files! All your edits must be inside your server's folder.**

## IP Addresses

The `addresses` array in each server object is actually an array of IP _suffixes_. For example, `"addresses": ["goldenpvp.net", "other.domain"]` will match `goldenpvp.net`, `na.goldenpvp.net`, `play.other.domain`, and so on. The `primaryAddress` field is where you can include the desired subdomain (`na.goldenpvp.net`, `play.goldenpvp.net`) for users to connect to your server on and is required to be resolvable. This primary address will be used to ensure that the server remains online and active.

## Primary Info & Minecraft Versions

We also require your server's primary connection information and allowed client versions. The `primaryAddress` field should be an address **included** in the `addresses` array.

The `minecraftVersions` field must be an array of client versions allowed on your Minecraft server. *(ie. 1.7.10, 1.8.9)*; The `primaryMinecraftVersion` field must be a subversion of a major version included in the `minecraftVersions` array. **The versions you include must be versions that are directly offered in CheatBreaker**, which can be found in the version selector of the CheatBreaker Launcher.

If your server supports all of the subversions within a major version, you can list the version in `minecraftVersions` as `1.7.*`, but you will still need to specify the specific subversion in the `primaryMinecraftVersion` as this is the specific version that the client uses to Launch you into the game for Quick Connecting.

## Logos

In addition to the data that you will need to provide in your `metadata.json`, you will need to upload a `.png` version of your logo (108x108 `logo.png`), a server icon (64x64 `icon.png`) and a Discord logo (between 512x512 & 1024x1024 `discord.png`) into the same folder. All images are to be _transparent_, with the exception of the Discord logo, which can have a background.

## Backgrounds

**Partnered servers** are also required to provide background images, you will need to upload a `.png` version of the primary background (774x363 `primarybackground.png`) and a secondary background (447x172 `secondarybackground.png`) into the same folder as your `metadata.json`. Images should represent either the artistic style or the content of the server. Backgrounds should be free of marketing, text, and/or any logos (on the primary background) (that isn't part of a build).

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

CheatBreaker reserves the right to omit any servers.

## Problematic Enforcement

While this will be rare. If a server is found to be problematic for our userbase, we will add it to the `problematic.json`. The list will go as follows:

### Mark

The server has been deemed problematic, but no further decision has been made yet. If the server continues to be problematic after 7-30 days, the server will then proceed one or more levels as shown below.

### Minor

The server has caused issues with our userbase, but is only for a minor reason. This includes but is not limited to:

- Client crashes from the server
- API tampering
- Misinformation directly related to our services

Users will encounter a 10 second, skippable warning prompt upon attempting to join the server.

### Unsafe

The server has been deemed unsafe; however, users will still be allowed to join. Reasons may include:

- Failure to keep playerbase safe from any malicious activity
- Sensitive data breach. This will only be for one time offensives
- Extreme lack of rule enforcement from server moderation team.

Users will encounter a 30 second, non skippable warning prompt. The server will also not be promoted on our client Discord RPC, and will instead show that they are playing on an unsafe server.

### Block

The server has been deemed problematic to where we do not feel comfortable allowing users to join the server. Reasons may include:

- Malicious activity from ownership or developers
- Repeated sensitive data breaches
- Disallowing CheatBreaker services without any proper communication to us

Users will not be able to join the server through our services.

## Inactive Server Policy

If a server has closed down or has not been joinable for at least 3 months, we will add it to the `inactive.json`. This just flags our internal systems to not include the server in various place, but still retains all of the branding and other metadata you submit.

If you think your server has been added to this list by mistake, please create a new [issue](https://github.com/CheatBreakerNet/Client-API/issues).

## Any other questions?

Please create a new [issue](https://github.com/CheatBreakerNet/Client-API/issues) for any additional questions.
