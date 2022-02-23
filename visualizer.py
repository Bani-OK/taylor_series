import argparse
from math import sqrt

from manim import *
from tqdm import tqdm


def get_args():
    parser = argparse.ArgumentParser(
        description='Visualizes taylor series'
    )
    parser.add_argument(
        'num',
        type=int,
        default=13,
        help='amount of additions in taylor series',
        metavar='num'
    )
    parser.add_argument(
        '-q',
        choices=['l', 'm', 'h'],
        help='quality of the rendered video '
             '(l - 480p15, m - 720p30, h - 1080p60)',
        metavar='quality'
    )
    parser.add_argument(
        '-f',
        choices=['gif', 'mp4', 'mov', 'webm'],
        help='format of the rendered video (gif, mp4, mov, webm)',
        metavar='format'
    )
    return (parser.parse_args().num,
            parser.parse_args().q,
            parser.parse_args().f)


class MainScene(VectorScene):
    CONFIG = {
        "x_min": -14,
        "x_max": 14,
        "y_min": 0,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2)
    }

    def __init__(self, number):
        self.number = number
        VectorScene.__init__(self)

    def construct(self):
        axes = self.configure_axes()
        self.configure_given_func(axes)
        self.taylor_series(axes, self.number)

    def configure_given_func(self, axes):
        given_func = axes.plot(
            lambda x: np.sqrt(1 - 2 * x + 4 * x * x),
            color=ORANGE,
            x_range=[-0.9, 1.4]
        )
        label = axes.get_graph_label(given_func,
                                     r"\sqrt{1-2x+4x^2}",
                                     x_val=-1.4,
                                     direction=DOWN * 45)
        self.play(Create(given_func), Write(label))
        self.wait(1)

    def configure_axes(self):
        axes = Axes(
            x_range=[-1.4, 1.4, 0.1],
            y_range=[0.8, 2.3, 0.1],
            x_length=13,
            y_length=7,
            axis_config={"color": WHITE},
            y_axis_config={"numbers_to_include": np.arange(0.9, 2.3, 0.3)},
            x_axis_config={"numbers_to_include": np.arange(-1.4, 1.5, 0.3)},
            tips=False,
        ).move_to(ORIGIN)
        self.play(Create(axes))
        self.wait(1)
        return axes

    def taylor_series(self, axes, number):
        functions = [lambda x: (sqrt(3) / 2)]
        function_graph = axes.plot(
            lambda x: functions[0](x),
            color=BLUE,
            use_smoothing=False
        )
        self.play(Create(function_graph))
        for idx in tqdm(range(1, number)):
            functions.append(
                (lambda index: lambda x: (
                        functions[index - 1](x) * (1.5 - index) * 16 *
                        ((x - 0.25) ** 2) / (index * 3)))(idx)
            )
            cur_function_graph = axes.plot(
                lambda x: min(1000, max(-1000, functions[-1](x))),
                color=YELLOW,
                use_smoothing=False
            )
            self.play(Create(cur_function_graph))
            t_function_graph = axes.plot(
                lambda x: min(1000, max(-1000,
                                        sum(map(lambda y: y(x), functions)))),
                color=BLUE,
                use_smoothing=False
            )
            self.play(Transform(cur_function_graph, t_function_graph),
                      Transform(function_graph, t_function_graph))
            self.remove(cur_function_graph)


if __name__ == '__main__':
    amount, quality, video_format = get_args()
    config.quality = {
        'h': 'high_quality',
        'm': 'medium_quality',
        'l': 'low_quality',
        None: 'high_quality'
    }[quality]
    config.verbosity = 'CRITICAL'
    config.progress_bar = 'none'
    config.format = 'mp4' if video_format is None \
        else video_format
    scene = MainScene(amount)
    scene.render()
    dir_path = os.path.join(scene.renderer.file_writer.movie_file_path,
                            os.path.pardir)
    print(f'Movie has been saved at '
          f'{os.path.normpath(dir_path)}')
