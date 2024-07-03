o
    ��f  �                   @   s\   d dl Z d dlZdZdZdd� Zdg fdd�Zd	d
� Zdd� Zdd� Ze	dkr,e�  dS dS )�    Nz9I don't like eating anything because I'm a bot obviously!zPIf I were you, I would go to the internet and type exactly what you wrote there!c                  C   s   g d�} t �| �S )N)z Could you please re-phrase that?zI didn't get it.zSounds about right.z%Yeah, cool! Can you please elaborate?zWhat does that mean?z5I'm not sure I understand. Could you explain further?z!That's interesting! Tell me more.z-Sorry, I'm not programmed to understand that.zHmm, can you clarify?z$I'm not sure how to respond to that.z,Could you say that again in a different way?)�random�choice)�	responses� r   �bC:\Users\Divya\Downloads\text_recogniton_chat-master\text_recogniton_chat-master\long_responses.py�unknown   s   
r   Fc                 C   sh   d}d}| D ]
}||v r|d7 }qt |�t t|�� }|D ]
}|| vr'd} q(q|s,|r2t|d �S dS )Nr   T�   F�d   )�float�len�int)�user_message�recognised_words�single_response�required_words�message_certainty�has_required_words�word�
percentager   r   r   �message_probability   s   ��r   c                    s�   i � dg f� �fdd�	}|dg d�dd� |dd	d
gdd� |dg d�dgd� |dddgdd� |dg d�ddgd� |dg d�dd� |t ddgdgd� |tg d�ddgd� t� � jd�}� | dk rjt� S |S )NFc                    s   t �|||�� | < d S )N)r   )�bot_response�list_of_wordsr   r   ��highest_prob_list�messager   r   �response4   s   z$check_all_messages.<locals>.responsezHello!)�hello�hi�hey�sup�heyoT)r   zSee you!�bye�goodbyezI'm doing fine, and you?)�how�are�you�doingr#   )r   zYou're welcome!�thank�thanksz
Thank you!)�i�love�code�palacer+   r,   zGreat!)ZsoundsZgoodZGood�toZhear�give�advice)�whatr%   �eatr%   r1   )�keyr   )�R_ADVICE�R_EATING�max�getr   )r   r   �
best_matchr   r   r   �check_all_messages0   s   r8   c                 C   s   t �d| �� �}t|�}|S )Nz\s+|[,;?!.-]\s*)�re�split�lowerr8   )�
user_input�split_messager   r   r   r   �get_responseI   s   r>   c                  C   sX   t d� 	 td�} | �� dkrt d� d S | �� dkr t d� qt| �}t d|� �� q)	Nz(Bot: Hi there! How can I help you today?TzYou: �exitzBot: Goodbye!� zBot: Please say something.zBot: )�print�inputr;   �stripr>   )r<   r   r   r   r   �run_botO   s   �rD   �__main__)
r9   r   r4   r3   r   r   r8   r>   rD   �__name__r   r   r   r   �<module>   s    
�