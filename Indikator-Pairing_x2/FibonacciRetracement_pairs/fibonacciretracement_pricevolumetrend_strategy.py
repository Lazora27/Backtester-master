import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
