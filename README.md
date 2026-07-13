# <span style="color: #2853aa">GenTact Toolbox</span>: A Design Platform for Procedurally Generated Artificial Skins

[![arXiv](https://img.shields.io/badge/arXiv-2412.00711-df2a2a.svg?style=for-the-badge)](https://arxiv.org/abs/2412.00711)
[![Isaac Sim Extension](https://img.shields.io/badge/Isaac%20Sim%20Extension-4.0.0%20-76B900?style=for-the-badge)](isaac_contact_ext/README.md)
[![Blender Add-on](https://img.shields.io/badge/Blender%20Add--on-4.5+%20-EA7600?style=for-the-badge)](procedural_skins_addon/README.md)
<!-- [![License](https://img.shields.io/github/license/TRI-ML/prismatic-vlms?style=for-the-badge)](LICENSE) -->
 
[**Website**](https://hiro-group.ronc.one/gentacttoolbox) | [**Getting Started**](#getting-started) | [**Making Your First Skin**](#making-your-first-skin) | [**Tips and Tricks**](#tips-and-tricks) | [**More Modalities**](#more-modalities)

<hr style="border: 2px solid gray;"></hr>

Procedural skins are a new class of artificial skins for robotic applications designed to be form-fitting and highly customizable to individual robots and use-cases. Procedural skins utilize a CAD model of a robot to automatically generate sensors with directely tunable parameters such as sensor density and sensing coverage are directly tunable.

# Prerequisites
Procedural skins are designed in [Blender](https://www.blender.org/download/releases/4-1/), then can be optimized or deployed in simulation through [Isaac Sim](https://developer.nvidia.com/isaac/sim). The procedural skins developed here use [RC delay capacitive sensing](https://sandrabae.github.io/sensing-network/index.html) and are fabricated using multi-material 3D prinitng. Please refer to the [original paper](https://arxiv.org/abs/2412.00711) for more information on fabrication.

# Getting Started

No prerequisite experience with Blender is needed to get started and design your first skin unit. All you need is a CAD model that you plan to cover with skin, then drag and drop the desired components onto the model from the asset browser.

## Blender Procedural Generation Add-on:

Detailed instructions on how to design your first skin unit can be found in the [Blender Procedural Generation Add-on README](procedural_skins_addon/README.md)
<hr style="border-top: 3px solid #EA7600;">

## Isaac Sim Contact Extension:
Detailed instructions on how to import your skin unit to Isaac Sim can be found in the [Contact Extension README](isaac_contact_ext/README.md)
<hr style="border-top: 3px solid #76B900;">


# Making your first skin
[Tutorial video!](https://youtu.be/qH5VpunpglI)
<!-- 
# Tips and tricks

# More Modalities -->

# Creating a Custom Procedural Algorithm

The procedural design is built on Blender's geometry node system. You can edit the designs by opening a geometry nodes window and navigating through the premade tabs.

# Building the Extension
```bash
cd procedural_skins_addon
blender --command extension build
```
Import the zip file via Edit > Preferences > Get Extensions > Install from Disk

# Liscence

This repository is under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/), which allows for unrestricted sharing and modifications with attribution, but prohibits commercial use.

## Citation

If you find our paper or codebase helpful, please consider citing:

```
@inproceedings{kohlbrenner2025gentact,
  title={Design, Mapping, and Contact Anticipation with 3D-printed Whole-Body Tactile and Proximity Sensors},
  author={Kohlbrenner, Carson and Soukhovei, Anna and Escobedo, Caleb and Nechyporenko, Nataliya and Roncone, Alessandro},
  booktitle={2026 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2026}
}

@inproceedings{kohlbrenner2025gentact,
  title={GenTact Toolbox: A Computational Design Pipeline to Procedurally Generate Context-Driven 3D Printed Whole-Body Artificial Skins},
  author={Kohlbrenner, Carson and Escobedo, Caleb and Bae, S Sandra and Dickhans, Alexander and Roncone, Alessandro},
  booktitle={2025 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2025}
}
```

