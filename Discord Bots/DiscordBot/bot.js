var Discord = require("discord.io");

var logger = require("winston");

var auth = require("./auth.json");

// Configure logger settings

logger.remove(logger.transports.Console);

logger.add(new logger.transports.Console(), {
  colorize: true,
});

logger.level = "debug";

// Initialize Discord Bot

var bot = new Discord.Client({
  token: auth.token,

  autorun: true,
});

bot.on("ready", function (evt) {
  logger.info("Connected");

  logger.info("Logged in as: ");

  logger.info(bot.username + " - (" + bot.id + ")");
});

bot.on("message", function (user, userID, channelID, message, evt) {
  // Our bot needs to know if it will execute a command

  // It will listen for messages that will start with `!`

  if (message.substring(0, 1) == "!") {
    var args = message.substring(1).split(" ");

    var cmd = args[0];

    // args = args.splice(1);

    switch (cmd) {
      // !ping

      case "ping":
        bot.sendMessage({
          to: channelID,

          message: "Pong!",
        });

        break;
      case "zobair":
        bot.sendMessage({
          to: channelID,

          message: "najdaoui",
        });

        break;
      case "intro":
        bot.sendMessage({
          to: channelID,
          message: "This is an introduction message!",
        });
        break;
      case "help":
        bot.sendMessage({
          to: channelID,

          message: "I can help you with commands, info, and support!",
        });

        break;

      case "commands":
        bot.sendMessage({
          to: channelID,

          message: "Type !help to see a list of commands.",
        });

        break;

      case "uptime":
        bot.sendMessage({
          to: channelID,

          message: "I have been running for X minutes.",
        });

        break;

      case "info":
        bot.sendMessage({
          to: channelID,

          message:
            "I'm a bot created by [Name] to help you with commands and info.",
        });

        break;

      case "support":
        bot.sendMessage({
          to: channelID,

          message:
            "If you need any help or support, contact [Name] at [Email].",
        });

        break;

      case "invite":
        bot.sendMessage({
          to: channelID,

          message: "Click this link to invite me to your server: [Link]",
        });

        break;

      case "say":
        bot.sendMessage({
          to: channelID,

          message: args.join(" ").substring(4),
        });

        break;

      case "choose":
        var choices = args.slice(1).join(" ").split(" or ");

        var choice = choices[Math.floor(Math.random() * choices.length)];

        bot.sendMessage({
          to: channelID,

          message: choice,
        });

        break;

      case "roll":
        var rolls = args[1] || 6;
        var sides = args[2] || 6;

        var total = 0;

        for (var i = 0; i < rolls; i++) {
          total += Math.floor(Math.random() * sides) + 1;
        }

        bot.sendMessage({
          to: channelID,

          message: "You rolled " + total + "!",
        });

        break;

      // Just add any case commands if you want to..
    }
  }
});
