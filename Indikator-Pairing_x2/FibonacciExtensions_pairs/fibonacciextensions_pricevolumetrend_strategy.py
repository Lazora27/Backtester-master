import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
