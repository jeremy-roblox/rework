class HowbloxException(Exception):
    def __init__(self, message=None, type="error", dm=False, hidden=False):
        self.type = type
        self.dm = dm # only implemented in a few places
        self.hidden = hidden
        self.message = message


class CancelCommand(HowbloxException):
    pass

class Messages(CancelCommand):
    def __init__(self, *args, type="send", **kwargs):
        super().__init__(*args, type=type, **kwargs)

class Message(Messages):
    def __init__(self, *args, type="send", **kwargs):
        super().__init__(*args, type=type, **kwargs)

class Error(Messages):
    def __init__(self, *args, type="send", **kwargs):
        super().__init__(*args, type=type, **kwargs)

class CancelledPrompt(CancelCommand):
    def __init__(self, *args, type="send", **kwargs):
        super().__init__(*args, type=type, **kwargs)

class PermissionError(HowbloxException):
    pass

class BadUsage(HowbloxException):
    pass

class RobloxAPIError(HowbloxException):
    pass

class RobloxNotFound(HowbloxException):
    pass

class RobloxDown(HowbloxException):
    pass

class UserNotVerified(HowbloxException):
    pass

class BloxlinkBypass(HowbloxException):
    pass

class Blacklisted(HowbloxException):
    def __init__(self, *args, guild_restriction=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.guild_restriction = guild_restriction
