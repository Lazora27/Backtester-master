import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
