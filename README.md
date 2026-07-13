# <span style="color: #2853aa">GenTact Toolbox</span>: Procedurally Generated Tactile Skin for Robots

[![arXiv](https://img.shields.io/badge/arXiv-2412.00711-df2a2a.svg?style=for-the-badge)](https://arxiv.org/abs/2412.00711)
[![Isaac Sim Extension](https://img.shields.io/badge/Isaac%20Sim%20Extension-4.0.0%20-76B900?style=for-the-badge)](isaac_contact_ext/README.md)
[![Blender Add-on](https://img.shields.io/badge/Blender%20Add--on-5.1+%20-EA7600?style=for-the-badge)](procedural_skins_addon/README.md)
<!-- [![License](https://img.shields.io/github/license/TRI-ML/prismatic-vlms?style=for-the-badge)](LICENSE) -->
 
[**Website**](https://hiro-group.ronc.one/gentacttoolbox) | [**Getting Started**](#getting-started) | [**Making Your First Skin**](#making-your-first-skin) | [**Tips and Tricks**](#tips-and-tricks) | [**More Modalities**](#more-modalities)

<hr style="border: 2px solid gray;"></hr>

Procedural skins are a new class of artificial skins for robotic applications designed to be form-fitting and highly customizable to individual robots and use-cases. Procedural skins utilize a CAD model of a robot to automatically generate sensors with directely tunable parameters such as sensing resolution and sensing coverage.

# Making your first skin

<p align="center">
  <a href="https://youtu.be/qH5VpunpglI">
    <img src="https://img.youtube.com/vi/qH5VpunpglI/maxresdefault.jpg" alt="Watch the video" width="70%">
  </a>
  <br>
  <a href="https://youtu.be/qH5VpunpglI">
    <img src="https://img.shields.io/badge/▶-Tutorial%20video-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Tutorial video">
  </a>
</p>

# Installation

## Intallation via ZIP (Recommended, all platforms)

Download the [latest release here](https://github.com/HIRO-group/GenTact/releases). Once downloaded, import the extension in Blender via *Edit > Preferences > Get Extensions > Install from Disk...*

## Installation from source (For Development, Linux and Mac)

```bash
./install.sh
```
This script will automatically find your Blender version, then generate a built copy of the extension under *build*.
The zip file in *build* containing the extension can be installed in Blender via *Edit > Preferences > Get Extensions > Install from Disk...*


### Alternative Installation 

Each node is provided as an *Asset* and can be accessed through the *Asset Browser* in Blender. To add the nodes to the *Asset Browser*, include the path to the *procedural_skins_addon* through the following steps in Blender:
1) Navigate to *Edit* > *Preferences*
2) Add *procedural_skins_addon* to the Asset Libraries file paths ![Preferences image](resources/preferences.png)
*Note: This approach is no longer supported by our team and may result in some geometry nodes being unavailable*

# Getting Started

No prerequisite experience with Blender is needed to get started and design your first skin unit. All you need is a CAD model that you plan to cover with skin, then drag and drop the desired components onto the model from the asset browser.


# Creating a Custom Procedural Algorithm

The procedural design is built on Blender's geometry node system. You can edit the designs by opening a geometry nodes window and navigating through the premade tabs.

## Isaac Sim Contact Extension:

<hr style="border-top: 3px solid #76B900;">

Detailed instructions on how to import your skin unit to Isaac Sim can be found in the [Contact Extension README](isaac_contact_ext/README.md)


# Liscence

This repository is under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/), which allows for unrestricted sharing and modifications with attribution, but prohibits commercial use.

## Citation

If you find our paper or codebase helpful, please consider citing:

```
@inproceedings{kohlbrenner2026design,
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

