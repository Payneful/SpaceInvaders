from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        messages = cast.get_actors("messages")
        bullets = cast.get_actors("bullets")
        ships = cast.get_actors("ships")
        explosions = cast.get_actors("explosions")
        lives = cast.get_first_actor("lives")
        background = cast.get_first_actor("background")

        self._video_service.clear_buffer()
        self._video_service.draw_actor_image(background)
        self._video_service.draw_actor_images(bullets)
        if snake != None:
            self._video_service.draw_actor_image(snake)
        self._video_service.draw_actor_images(ships)
        self._video_service.draw_actor_images(explosions)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(lives)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()