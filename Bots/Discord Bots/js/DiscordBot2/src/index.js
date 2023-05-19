const { Client, IntentsBitField } = require("discord.js");

const client = new Client({
  intents: [
    IntentsBitField.Flags.Guilds,
    IntentsBitField.Flags.GuildMembers,
    IntentsBitField.Flags.GuildMessages,
    IntentsBitField.Flags.MessageContent,
  ],
});


client.login(
  "MTA4MTk3MDUzMjU4MjQyODcwMw.Gof4jm.mrF8rBtcXJh1u_MgK9SiJT14K4eZNy4SmztVgE"
);
