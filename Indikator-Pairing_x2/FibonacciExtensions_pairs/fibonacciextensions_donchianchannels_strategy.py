import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'DonchianChannels': 1.0
        })
    )
