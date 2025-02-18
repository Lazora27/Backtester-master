import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciVolumeRatio_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciVolumeRatio und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FibonacciVolumeRatio': 1.0,
            'TrendCycles': 1.0
        })
    )
