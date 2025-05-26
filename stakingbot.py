
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7862781299:AAHcg3xdVHqTftKuQfTh3CFSyqN0VPxXDC4"
app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎁 *Welcome to USDT Quantify Staking!*\n"
        "🔥 Register now and get started instantly: [Start Earning](https://layer.top/#/register?ref=867875)\n\n"
        "📈 Stake to earn stable daily profit – no price volatility.\n"
        "🎉 Don't miss your chance to qualify for the 8888 USDT lucky draw!",
        parse_mode="Markdown"
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 *Claim Daily Profit*\n"
        "1. Click the link ➡️ [Quantify Now](https://layer.top/#/register?ref=867875)\n"
        "2. Tap *Quantify* to collect your daily earnings.\n"
        "💸 Profits updated daily, don't miss out!",
        parse_mode="Markdown"
    )

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💵 *How to Withdraw*\n"
        "Simply link your wallet:\n"
        "- USDT (BEP20)\n"
        "- USDC (BEP20)\n\n"
        "⚡ Fast & secure withdrawal to your wallet. Withdrawal opens after linking.",
        parse_mode="Markdown"
    )

async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 *Join the Official Community*\n"
        "Still have questions or want real-time support?\n\n"
        "👥 Join our Telegram group for updates, guides, and exclusive tips:\n"
        "👉 [Join Now](https://t.me/+t0aBYQK8SxUwODQ1)",
        parse_mode="Markdown"
    )

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 *Upgrade VIP & Win Big!*\n"
        "The higher your VIP level, the more lottery chances & daily profit you get! 🎰\n\n"
        "🎯 *Investment Tiers:*\n"
        "- 💰 10 USDT → Earn 22 USDT total | ~0.8 USDT/day | 1 lottery draw/day\n"
        "- 💰 100 USDT → Earn 112 USDT total | ~3.8 USDT/day | 5 draws/day\n"
        "- 💰 500 USDT → Earn 512 USDT total | ~18 USDT/day | 18 draws/day\n"
        "- 💰 1000 USDT → *Become a Senior Manager* | Unlock friend referral bonus (up to 16%)\n"
        "- 💰 5000 USDT → 58 cumulative lottery chances\n"
        "- 💰 10000 USDT → 128 chances\n"
        "- 💰 50000 USDT → 588 chances\n"
        "- 💰 100000 USDT → 1588 chances\n"
        "- 💰 500000 USDT → 5888 chances\n"
        "- 💰 1000000 USDT → 🚀 *8888 LOTTERY DRAWS!*\n\n"
        "🎉 More VIP = More Fun + More Earnings!",
        parse_mode="Markdown"
    )

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎁 *Invite & Win – Referral Program*\n"
        "🔗 Invite your friends and earn *lottery chances* worth up to **8888 USDT**!\n\n"
        "✅ For every friend who invests 10 USDT cumulatively,\n"
        "🎟️ You get 1 extra chance to win the lucky prize.\n\n"
        "📈 More friends = More rewards = Bigger lottery shots!",
        parse_mode="Markdown"
    )

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check", check))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("guide", guide))
app.add_handler(CommandHandler("vip", vip))
app.add_handler(CommandHandler("referral", referral))

if __name__ == '__main__':
    app.run_polling()
