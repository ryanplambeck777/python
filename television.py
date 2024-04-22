class Television:
    """A class representing a television"""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the television with default values"""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        self.__previous_volume: int = self.MIN_VOLUME  # To store the volume before muting

    def power(self) -> None:
        """Toggle the power of the television"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute of the television"""
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume  # Restore previous volume
            else:
                self.__previous_volume = self.__volume  # Remember current volume
                self.__volume = self.MIN_VOLUME  # Set volume to 0 when muting
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel by 1"""
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the channel by 1"""
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increase the volume by 1"""
        if self.__status:
            if self.__muted:
                self.mute()  # Unmute before adjusting volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by 1"""
        if self.__status:
            if self.__muted:
                self.mute()  # Unmute before adjusting volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Print the television object"""
        power_status = "True" if self.__status else "False"
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}"
