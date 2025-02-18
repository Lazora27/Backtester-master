import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'KeltnerChannels': 1.0
        })
    )
