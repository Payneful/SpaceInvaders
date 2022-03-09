import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, x_position, _snake):
        super().__init__()
        self._segments = []
        self._prepare_body(x_position, _snake)
        self._snake = _snake

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            if self._snake == 0:
                color = constants.GREEN
            elif self._snake == 1:
                color = constants.RED
            elif self._snake == 2:
                color = constants.BLUE
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, x_position, _snake):
        x = int(x_position)
        y = int(constants.MAX_Y / 2)
        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y - i * constants.CELL_SIZE)
            velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            if _snake == 0:
                color = constants.GREEN
            elif _snake == 1:
                color = constants.RED
            elif _snake == 2:
                color = constants.BLUE
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)