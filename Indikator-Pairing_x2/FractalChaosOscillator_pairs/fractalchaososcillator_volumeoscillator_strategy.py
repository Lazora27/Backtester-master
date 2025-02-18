import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'VolumeOscillator': 1.0
        })
    )
