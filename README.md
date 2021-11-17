# dice-roll-albert-ext

[![discord](https://custom-icon-badges.herokuapp.com/discord/819650821314052106?color=5865F2&logo=discord-outline&logoColor=white "Dev Pro Tips Discussion & Support Server")](https://discord.gg/fPrdqh3Zfu)
[![License MIT](https://custom-icon-badges.herokuapp.com/github/license/DenverCoder1/dice-roll-albert-ext.svg?logo=repo)](https://github.com/DenverCoder1/dice-roll-albert-ext/blob/main/LICENSE)
[![code style black](https://custom-icon-badges.herokuapp.com/badge/code%20style-black-black.svg?logo=black-b&logoColor=white)](https://github.com/psf/black)

Extension for rolling dice in [Albert launcher](https://albertlauncher.github.io/)

![demo gif](https://user-images.githubusercontent.com/20955511/142091472-aaa53beb-2259-4b72-8aa4-4f1419741570.gif)

## Installation

1. Locate the `modules` directory in the Python extension data directory.

The data directories reside in the data directories of the application defined by Qt. Hence on linux the modules would be looked up in the following directories (in this order):

```
~/.local/share/albert/org.albert.extension.python/modules
/usr/local/share/albert/org.albert.extension.python/modules
/usr/share/albert/org.albert.extension.python/modules
```

Double-clicking on a module in the settings will open the directory in the file manager.

2. Clone this repository into your `modules` directory.

```bash
cd /path/to/modules

git clone https://github.com/DenverCoder1/dice-roll-albert-ext.git
```

## Usage

Roll any number of dice using the format `_d_`.

Synopsis: `<amount>d<sides> [<amount>d<sides> ...]`

Example: `"2d6 3d8 1d20"`

## Contributing

If you have any questions, suggestions, or issues, please feel free to open an issue or pull request.

## Support

💙 If you like this project, give it a ⭐ and share it with friends!

<p align="left">
  <a href="https://www.youtube.com/channel/UCipSxT7a3rn81vGLw9lqRkg?sub_confirmation=1"><img alt="Youtube" title="Youtube" src="https://custom-icon-badges.herokuapp.com/badge/-Subscribe-red?style=for-the-badge&logo=video&logoColor=white"/></a>
  <a href="https://github.com/sponsors/DenverCoder1"><img alt="Sponsor with Github" title="Sponsor with Github" src="https://custom-icon-badges.herokuapp.com/badge/-Sponsor-ea4aaa?style=for-the-badge&logo=heart&logoColor=white"/></a>
</p>

[☕ Buy me a coffee](https://ko-fi.com/jlawrence)