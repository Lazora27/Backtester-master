import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'KeltnerChannels': 1.0
        })
    )
