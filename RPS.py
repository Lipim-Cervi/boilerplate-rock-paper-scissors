def player(prev_play, opponent_history=[], play_order=[{}, {}, {}, {}, {}]):

    if not prev_play:
        # Nova partida: limpa tudo
        opponent_history.clear()
        for i in range(5):
            play_order[i] = {}
        prev_play = "R"

    opponent_history.append(prev_play)

    # O que ganha de cada jogada
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    guess = "R"

    # Tenta padrões de tamanho 5, 4, 3, 2, 1
    for i, n in enumerate([5, 4, 3, 2, 1]):
        if len(opponent_history) > n:
            # Registra o padrão no dicionário correspondente
            pattern = "".join(opponent_history[-n:])
            play_order[i][pattern] = play_order[i].get(pattern, 0) + 1

    # Usa o maior padrão que tiver dados para prever
    for i, n in enumerate([5, 4, 3, 2, 1]):
        if len(opponent_history) > n:
            last = "".join(opponent_history[-(n - 1):]) if n > 1 else ""
            potential_plays = [last + "R", last + "P", last + "S"]

            sub_order = {k: play_order[i].get(k, 0) for k in potential_plays}

            if max(sub_order.values()) > 0:
                prediction = max(sub_order, key=sub_order.get)[-1]
                # Contra-ataca: o que ganha da jogada prevista
                guess = ideal_response[prediction]
                break

    return guess


