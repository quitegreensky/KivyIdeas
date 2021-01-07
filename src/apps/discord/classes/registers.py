from kivy.factory import Factory

r = Factory.register

r("CardNavigation", module="apps.discord.classes.uix.navigation_layout")
r("MenuCardRight", module="apps.discord.classes.uix.navigation_layout")
r("MenuCardLeft", module="apps.discord.classes.uix.navigation_layout")
r("MenuFrontCard", module="apps.discord.classes.uix.navigation_layout")
r("LeftMenu", module="apps.discord.classes.uix.left_menu")
r("FrontMenu", module="apps.discord.classes.uix.front_menu")
r("RightMenu", module="apps.discord.classes.uix.right_menu")
r("DiscordToolbar", module="apps.discord.classes.uix.toolbar")
r("DiscordToolbarButton", module="apps.discord.classes.uix.toolbar")
r("DiscordChannelListItem", module="apps.discord.classes.uix.channel_list")
r("DiscordChannelList", module="apps.discord.classes.uix.channel_list")
r("DiscordLabel", module="apps.discord.classes.uix.label")
r("DiscordIcon", module="apps.discord.classes.uix.avatar")
r("DiscordChannelIcons", module="apps.discord.classes.uix.channel_icon")
r("DiscordChannelInfo", module="apps.discord.classes.uix.channel_info")
r("DiscordTextIconButton", module="apps.discord.classes.uix.button")
r("DiscordTextFieldButton", module="apps.discord.classes.uix.button")
r("DiscordTextField", module="apps.discord.classes.uix.textfield")
r("DiscordBottomNavigation", module="apps.discord.classes.uix.bottom_navigation")
r("DiscordBottomNavigationIcon", module="apps.discord.classes.uix.bottom_navigation")
