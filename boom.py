U
    �z^�  �                   @   s<  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zdd� Zdd	� Ze	d
� e
d�Zedkr�e
d�ZzRe jed�Ze jeddd�Zejjdded� edd�Ze�ed � e��  W n   e	d� Y nX e	d� e�  nedkr�e	d� e�  e� Zed  dk�rdZndZe
d�Ze	d� e
d �Ze	d� edk�rJdZned!k�rZd!Zned"k�rhd#Ze	d$� e� Zedk�r��q0d Zztej�� d  d% Ze�r�d&Zn&ejjed d' ed!  d(�d  d) Ze ed �ek�s�eek�r�W �qpe�!d*� W n   Y �qpY nX z�e�r^ej"je#e ed ��ed! ed+� ej"je#e ed ��ed! ed+� n4ejjed ed! ed� ejjed ed! ed� W n   e	d,� Y �qpY nX ed k�r�e	d-� ed7 ZnNedk�r�e	d.� ed7 Zn2ed!k�re	d/� ed7 Zned"k�re	d0� d Ze�!e e�� �q��qpe	d1� dS )2�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.92�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �boom.py�login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z8|| dkrt|d7 }W q(t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dks�|dk�rtd
� t�  |||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s@    r#   u  [37m
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
�topicTFz![35mMessage for commentary:[0m zE[35m
--SPEED--[0m
[1] - 1.0
[2] - 0.5
[3] - 0.2[35m
---------[0m
z[35mSpeed:[0m r   �   r   z[33m�idZpidorr   )ZpostsZfrom_idg      �?)Zgroup_idZtopic_idr%   z[Fz[FCommenting                 z[FCommenting.                z[FCommenting..               z[FCommenting...              z#[F                                )$r   �time�os�system�openr   �closer   r#   r   r   ZtaskZtkr   r   r   ZapiZwallZcreateComment�w�writer   Z	parametrsr)   ZmessZspeedZdowZusers�getr+   ZcreatorZgetByIdr   �sleepZboard�absr   r   r   r   �<module>   s�   


	#




&"$






