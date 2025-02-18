import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciVolumeRatio_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciVolumeRatio und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FibonacciVolumeRatio': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
