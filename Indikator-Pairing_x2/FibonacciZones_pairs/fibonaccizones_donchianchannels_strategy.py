import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DonchianChannels': 1.0
        })
    )
