import bot

def test_answer():
    assert bot.get_answer_msg("Новый заказ", None) == "Какую вы хотите пиццу? Большую или маленькую?"
    assert bot.get_answer_msg("start", None) == "Какую вы хотите пиццу? Большую или маленькую?"
    assert bot.get_answer_msg("/start", None) == "Какую вы хотите пиццу? Большую или маленькую?"
    assert bot.get_answer_msg("Большую", None) == "Как вы будете платить?"
    assert bot.get_answer_msg("Маленькую", None) == "Как вы будете платить?"
    assert bot.get_answer_msg("Наличкой", "Большую") == "Вы хотите Большую пиццу, оплата - Наличкой?"
    assert bot.get_answer_msg("Наличкой", "Маленькую") == "Вы хотите Маленькую пиццу, оплата - Наличкой?"
    assert bot.get_answer_msg("Картой", "Большую") == "Вы хотите Большую пиццу, оплата - Картой?"
    assert bot.get_answer_msg("Картой", "Маленькую") == "Вы хотите Маленькую пиццу, оплата - Картой?"
    assert bot.get_answer_msg("Да", None) == "Спасибо за заказ"
    assert bot.get_answer_msg("Нет", None) == "Ок, заказ отменен"

