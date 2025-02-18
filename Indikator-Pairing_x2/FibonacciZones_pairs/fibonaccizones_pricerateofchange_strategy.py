import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
