# GIF-Duration-Cutter
Crop GIFs easily with my new project! If you've seen my past work, you know I love using GIFs. Tired of slow or weird online tools? My project simplifies it all. Forget typing commands or frame numbers every time—this tool does it for you, showing total frames and letting you pick start and end frames for a perfect GIF!

## Application Variation Using Nautilus Scripts
![GIF Cutter (Nautilus Variation)](https://github.com/pefbrute/GIF-Duration-Cutter/blob/main/cut_How%20GIF%20Cutter%20(Nautilus%20Variation)%20Works.gif)

## Application Variation Without Nautilus Scripts
![GIF Cutter](https://github.com/pefbrute/GIF-Duration-Cutter/blob/main/cut_How%20GIF%20Cutter%20Works.gif)


## Installation
```
sudo apt install python3
sudo apt-get install python3-tk
sudo apt-get install gifsicle
sudo apt-get install nautilus
```

## How To Add Python Script to Nautilus Scripts
![Functionality](https://github.com/pefbrute/GIF-Duration-Cutter/blob/main/How%20To%20Add%20Script%20to%20Nautilus%20Scripts.gif)

1. Перейти В Папку Nautilus Scripts
```
nautilus ~/.local/share/nautilus/scripts
```
2. Создать питон скрипт, например, gif-cutter2.py
```
touch gif-cutter2.py
```

4. Внести в него код (он находится в gif-cutter-using-nautilus.py)

5. Сделать файл исполняемым
```
sudo chmod +x gif-cutter2.py
```
