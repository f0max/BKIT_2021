from bot.utils import TestStates
from bot.answers import *



help_message = 'Для того, чтобы изменить текущее состояние, ' \
               f'отправь команду "/setstate x", где x - число от 0 до {len(TestStates.all()) - 1}.\n' \
               '1 - выбор локации\n2 - сбор рюкзака\n3 - выбор способа перемещения\n0 - посмотреть, что получилось.\n' \
               'Чтобы сбросить текущее состояние, отправь "/setstate" без аргументов.'

start_message = 'Привет! Давай соберемся в поход.\n' + help_message
invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
state_reset_message = 'Состояние успешно сброшено'
first_state_message = 'Определимся, куда нам собираться:\n' \
                      f'0. {location[0]}\n' \
                      f'1. {location[1]}\n' \
                      f'2. {location[2]}' 
second_state_message = 'Что возьмем с собой?\n' \
                      f'0. {backpack[0]}\n' \
                      f'1. {backpack[1]}\n' \
                      f'2. {backpack[2]}' 
third_state_message = 'Как будем добираться?\n' \
                      f'0. {transport[0]}\n' \
                      f'1. {transport[1]}\n' \
                      f'2. {transport[2]}' 
null_state_message = 'Вот что получилось'
wrong_answer = 'Такого варианта ответа нет.\n' \
               'Выберите цифру из предложенного списка.'
success_answer = 'Ваш выбор успешно записан.\n' \
                 'Если хотите его изменить, снова введите цифру.\n' \
                 'Когда определитесь с выбором, можете переходить к следующему с помощью /setstate.\n' \
                 '/setstate 0 - чтобы посмотреть, что получилось.'
camp_message = 'В итоге:\n' \
               'Локация: {loc}.\n' \
               'В рюкзаке: {bp}.\n' \
               'Способ передвижения: {transp}.\n' \
               '/setstate, чтобы очистить и собрать заново.'

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'invalid_key': invalid_key_message,
    'state_reset': state_reset_message,
    0 : null_state_message,
    1 : first_state_message,
    2 : second_state_message,
    3 : third_state_message,
    'wrong_answer' : wrong_answer,
    'success_answer' : success_answer,
    'camp' : camp_message,
}