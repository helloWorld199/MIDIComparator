from dataclasses import dataclass

@dataclass
class MetricConfig:
    """
        List of metrics to use
    """
    bar_absolute_pitches: bool = False
    bar_pitch_variety: bool = False
    bar_note_density: bool = False
    note_durations: bool = False




