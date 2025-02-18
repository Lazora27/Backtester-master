import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'KeltnerChannels': 1.0
        })
    )
