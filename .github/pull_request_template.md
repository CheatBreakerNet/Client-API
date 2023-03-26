### General:
* [ ] The pull request title is descriptive. *(ex. `Added GoldenPvP Network`, not `Updated metadata.json`)*
* [ ] The pull request does not contain any unrelated commits.  *(ex. commits from previous pull requests)*

### Mapping Additions or Updates:
* [ ] Folder with appropriate name has been created / updated (must not include any non-alpha characters or whitespace).
* [ ] No changes were made to the file's formatting (4 spaces per tab).
* [ ] There are no syntax errors.
* [ ] There is no pre-existing mapping matching my id (check if there is an existing folder).
* [ ] My field values match your requirements.
* You can view our patterns here: [metadata.schema.json](https://github.com/Offline-CheatBreaker/Client-API/blob/master/mappings/metadata.schema.json), or take a look below and complete the field checklist:
  - [ ] `id`: a lowercase string, which should match the folder name *(ex. `goldenpvpnetwork`)*
  - [ ] `name`: a string *(ex. `GoldenPvP Network`)*
  - [ ] `description`: hook between 16 and 40 characters *(ex. `We're the home of classic PvP gamemodes`)* 
  - [ ] `addresses`: an array with lowercase strings *(ex. `["goldenpvp.net", "routing.center"]`)*
    - You do not need to specify subdomains, Offline CheatBreaker services automatically detect them.
  - [ ] `primaryAddress`: the primary address that people connect to with (please include the subdomain if required) *(ex. `mc.goldenpvp.net`)*
  - [ ] `minecraftVersions`: an array with Minecraft versions as strings *(ex. `["1.7.*", "1.8.9"]` - Must be versions or subversions supported by Offline CheatBreaker)*
  - [ ] `primaryMinecraftVersion`: a Minecraft version as a string *(ex. `1.7.10` - Must be a subversion supported by Offline CheatBreaker)*
  - [ ] `primaryColor`: a hexademical color code that primarily distinguishes the server *(ex. `#00FFFF`)* 
  - [ ] `secondaryColor`: a hexademical color code that accompanies the `primaryColor` of the server *(ex. `#FF0000`)*
  - [ ] `primaryRegion`: the primary region where your server operates in *(ex. `EU`)*
  - [ ] `regions`: a list of regions where you have servers located that service your players *(ex. `["EU", "NA", "AS"]`)*
  - [ ] `gameTypes`: a list of games that describe the content on your server, must be a max of 3 listed *(ez. `["PVP", "UHC", "HCF"]`)*
  - [ ] (optional) `website`: url of server website, must include URL schema (http:// or https://) *(ex. `https://www.goldenpvp.net`)*
  - [ ] (optional) `store`: url of server store, must include URL schema (http:// or https://) *(ex. `https://store.goldenpvp.net`)*

### Socials
* [ ] (optional) `twitter`: username of twitter account without the @ *(ex. GoldenPvPNet)*
* [ ] (optional) `discord`: invite link to discord *(ex. https://discord.com/invite/3EAzBxf)*
* [ ] (optional) `youtube`: slug or username of youtube channel *(ex. GoldenPvP)*
* [ ] (optional) `instagram`: username of instagram account *(ex. GoldenPvPNet)*
* [ ] (optional) `twitch`: username of twitch account *(ex. GoldenPvPNet)*
* [ ] (optional) `telegram`: slug of telegram group *(ex. GoldenPvP-Network)*
* [ ] (optional) `reddit`: slug of subdreddit wtih 'r/' *(ex. GoldenPvP)*
* [ ] (optional) `tiktok`: username of tiktok account *(ex. GoldenPvP)*
* [ ] (optional) `facebook`: slug of facebook page *(ex. GoldenPvP)*

### Media:
#### Icon
* [ ] My icon is a `png` file.
* [ ] I have uploaded my icon to my server folder *(ex. `goldenpvpnetwork`)* and named it `icon.png`.
* [ ] My icon has a transparent background and is square (1:1 aspect ratio).
* [ ] My icon is `64` pixels in width and height.
* [ ] My icon is my own property and complies with relevant copyright/privacy laws.

#### Logo
* [ ] My logo is a `png` file.
* [ ] I have uploaded my logo to my server folder *(ex. `goldenpvpnetwork`)* and named it `logo.png`.
* [ ] My logo has a transparent background and is square (1:1 aspect ratio).
* [ ] My logo is `108` pixels in width and height.
* [ ] My logo is my own property and complies with relevant copyright/privacy laws.

#### Discord Logo
* [ ] My logo is a `png` file.
* [ ] I have uploaded my logo to my server folder *(ex. `goldenpvpnetwork`)* and named it `discord.png`.
* [ ] My logo has a transparent background and is square (1:1 aspect ratio).
* [ ] My logo is between `512` and `1024` pixels in width and height.
* [ ] My logo is my own property and complies with relevant copyright/privacy laws.

#### Primary Background (Only required for partnered servers)
* [ ] My primary background is a `png` file.
* [ ] I have uploaded my primary background to my server folder *(ex. `goldenpvpnetwork`)* and named it `primarybackground.png`.
* [ ] My primary background is `774` pixels in width and `363` pixels in height.
* [ ] My primary background contains relevant content pertaining to the server, is my own property, and complies with relevant copyright/privacy laws.
* [ ] My primary background doesn't contain any markings, text, or logos (unless part of a build).

#### Secondary Background (Only required for partnered servers)
* [ ] My secondary background is a `png` file.
* [ ] I have uploaded my secondary background to my server folder *(ex. `goldenpvpnetwork`)* and named it `secondarybackground.png`.
* [ ] My secondary background is `447` pixels in width and `172` pixels in height.
* [ ] My secondary background contains relevant content pertaining to the server, is my own property, and complies with relevant copyright/privacy laws.
* [ ] My secondary background doesn't contain any markings, text, or logos (unless part of a build).
