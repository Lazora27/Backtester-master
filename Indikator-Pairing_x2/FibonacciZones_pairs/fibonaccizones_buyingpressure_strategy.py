import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'BuyingPressure': 1.0
        })
    )
