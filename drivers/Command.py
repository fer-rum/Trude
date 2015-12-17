__author__ = 'Fredo Erxleben'


class Command:
    """
    A command is build from a format string and a dictionary of arguments for this string.
    Commands may expect a reply. In this case they have to override the handle_reply function.
    Casting the command to a string will return the format string with the arguments applied.
    A command holds a list of allowed indices which has to be set by the inheriting class.
    Only arguments corresponding to one of the allowed indices can be assigned.
    """

    def __int__(self, format_string: str, arguments={}, expects_reply=False):
        self._expects_reply = expects_reply
        self._format_string = format_string
        self._arguments = arguments
        self._allowed_indices = ()

    @property
    def expects_reply(self):
        return self._expects_reply

    @property
    def allowed_indices(self):
        return self._allowed_indices

    def set_argument(self, index, value):
        if index in self._allowed_indices:
            self._arguments[index] = value
        else:
            raise ValueError("The given index was not in the list of allowed indices")

    def __str__(self):
        return self._format_string.format(self._arguments)

    def handle_reply(self, reply: str):
        """
        This has to be overridden by commands that actually expect replies.
        :param reply: The reply for the command you got from the device
        :return:
        """
        raise NotImplementedError("The command does not support reply handling")
