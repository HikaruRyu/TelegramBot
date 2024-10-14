from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


Token: Final = '7725937567:AAHohQsxDB1lO9-_MZX_rQ1lgnAMM095C1E'  # Token del bot
BOT_USERNAME: Final = '@LaGuardiola_Bot'  # Nom del Bot


# Comando /start
async def start_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global salary # Saldo actual
    global ingresos # Ingresos totals
    ingresos = 0 # Ingresos totals
    salary = ingresos
    await update.message.reply_text('Hello, How can I help you?')


# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "/help\n"
        "Aquí tens les comandes disponibles per al bot LA GUARDIOLA:\n"
        "/saldo: Mostra el teu saldo actual.\n"
        "/reserva: Consulta els diners que tens reservats per a l'estalvi.\n"
        "/introduirReserva: Permet introduir i actualitzar la quantitat que vols reservar per a estalvi.\n"
        "/despesses: Mostra el total de despeses acumulades.\n"
        "/quotesMensuals: Visualitza les despeses fixes mensuals.\n"
        "/introduirQuotesMensuals: Introdueix o actualitza les despeses mensuals.\n"
        "/gastosDiaris: Consulta les teves despeses diàries.\n"
        "/introduirGastosDiaris: Introdueix o actualitza les despeses diàries.\n"
        "/ganancies: Mostra els ingressos totals que tens.\n"
        "/introduirGananciesEsporadiques: Permet afegir ingressos esporàdics.\n"
        "/introduirGananciesMensuals: Introdueix o actualitza les teves guanyances mensuals."
    )
    await update.message.reply_text(help_text)


# Comando /saldo
async def saldo_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí puedes cambiar el valor por el saldo actual
    await update.message.reply_text(f'El teu saldo actual és de {salary}€')


# Comando /reserva
async def reserva_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    estalvi = 300  # Aquí puedes cambiar el valor de l'estalvi
    await update.message.reply_text(f'Has reservat {estalvi}€ per a l\'estalvi.')


# Comando /introduirReserva
async def introduir_reserva_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí se podría añadir lógica para introducir una nova quantitat d'estalvi
    await update.message.reply_text('Introduïu la quantitat d\'estalvi que voleu reservar.')


# Comando /despesses
async def despesses_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    despeses = 500  # Total despeses acumulades
    await update.message.reply_text(f'El total de les teves despeses fins al moment és de {despeses}€.')


# Comando /quotesMensuals
async def quotes_mensuals_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = 200  # Despeses mensuals fixes
    await update.message.reply_text(f'Les despeses mensuals fixes són de {quotes}€.')


# Comando /introduirQuotesMensuals
async def introduir_quotes_mensuals_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí se puede implementar la introducción de nuevas quotes mensuals
    await update.message.reply_text('Introduïu les noves quotes mensuals que voleu afegir.')


# Comando /gastosDiaris
async def gastos_diaris_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gastos_diaris = 50  # Despeses diàries
    await update.message.reply_text(f'Les despeses diàries fins ara són de {gastos_diaris}€.')


# Comando /introduirGastosDiaris
async def introduir_gastos_diaris_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí se puede implementar la introducción de nuevas despeses diàries
    await update.message.reply_text('Introduïu una nova despesa diària.')


# Comando /ganancies
async def ganancies_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Les teves ganàncies totals són de {ingresos}€.')


# Comando /introduirGananciesEsporadiques
async def introduir_ganancies_esporadiques_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí se puede implementar la introducción de ingressos esporàdics
    await update.message.reply_text('Introduïu els ingressos esporàdics que voleu afegir.')


# Comando /introduirGananciesMensuals
async def introduir_ganancies_mensuals_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí se puede implementar la introducción de ingressos mensuals
    await update.message.reply_text('Introduïu les ganàncies mensuals.')


# Respostes
def handle_response(text: str) -> str:
    processed: str = text.lower()
   
    if 'hello' in processed:
        return 'Hey there!'
    return 'I do not understand what you wrote'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text


    print(f'User ({update.message.chat.id}) in {message_type} : "{text}"')


    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
   
    print('Bot:', response)
    await update.message.reply_text(response)


# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Bot is running')
    app = Application.builder().token(Token).build()


    # Comandes
    app.add_handler(CommandHandler('start', start_))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('saldo', saldo_))
    app.add_handler(CommandHandler('reserva', reserva_))
    app.add_handler(CommandHandler('introduirReserva', introduir_reserva_))
    app.add_handler(CommandHandler('despesses', despesses_))
    app.add_handler(CommandHandler('quotesMensuals', quotes_mensuals_))
    app.add_handler(CommandHandler('introduirQuotesMensuals', introduir_quotes_mensuals_))
    app.add_handler(CommandHandler('gastosDiaris', gastos_diaris_))
    app.add_handler(CommandHandler('introduirGastosDiaris', introduir_gastos_diaris_))
    app.add_handler(CommandHandler('ganancies', ganancies_))
    app.add_handler(CommandHandler('introduirGananciesEsporadiques', introduir_ganancies_esporadiques_))
    app.add_handler(CommandHandler('introduirGananciesMensuals', introduir_ganancies_mensuals_))


    # Respostes
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    # Errors
    app.add_error_handler(error)


    # Polling
    print('Bot is polling')
    app.run_polling(poll_interval=3)
