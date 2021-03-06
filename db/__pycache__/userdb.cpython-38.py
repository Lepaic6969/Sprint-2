U
    l��_	  �                   @   s�   d dl mZmZ d dlmZ G dd� de�Zeeef Zef ddddd	d
ddd�d��ef ddddddd��ef ddddddd��ef ddddd d!d��d"�Zed#�d$d%�Zed&�d'd(�Z	d)S )*�    )�Dict�Optional)�	BaseModelc                   @   sN   e Zd ZU eed< eed< eed< eed< eed< eed< dZee ed< dS )	�UserInDB�email�password�name�	last_name�
department�	clearanceN�	documents)	�__name__�
__module__�__qualname__�str�__annotations__�intr   r   �dict� r   r   �.\db\userdb.pyr      s   
r   �cinthya@example.comZ
ejemplo123ZCinthyaZMurgasZGerencia�   z$https://docs.google.com/acuerdodepazzwww.reformatributaria.com)zAcuerdo de PazzReforma Tributaria)r   r   r   r	   r
   r   r   �martin@example.comZ
ejemplo987ZMartinZVasquezZFinanzas�   )r   r   r   r	   r
   r   �camilo@example.comZ
example345ZCamiloZZamoraZMercadeo�   �edwin@example.comZ
example123ZEdwinZGonzalezZVentas�   )r   r   r   r   �r   c                 C   s   | t �� krt |  S d S d S �N)�database_users�keysr   r   r   r   �get_user+   s    r"   ��
user_in_dbc                 C   s   | t | j< | S r   )r    r   r#   r   r   r   �update_user1   s    
r%   N)
�typingr   r   Zpydanticr   r   r   r    r"   r%   r   r   r   r   �<module>   sF   	�����