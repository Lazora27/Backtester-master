import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
