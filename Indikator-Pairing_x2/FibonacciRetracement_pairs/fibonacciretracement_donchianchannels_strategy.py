import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'DonchianChannels': 1.0
        })
    )
