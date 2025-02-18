import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'VolumeOscillator': 1.0
        })
    )
