import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FibonacciZones': 1.0
        })
    )
