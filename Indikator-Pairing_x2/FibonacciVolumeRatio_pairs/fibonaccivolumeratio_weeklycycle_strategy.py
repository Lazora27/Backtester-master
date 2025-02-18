import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciVolumeRatio_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciVolumeRatio und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FibonacciVolumeRatio': 1.0,
            'WeeklyCycle': 1.0
        })
    )
