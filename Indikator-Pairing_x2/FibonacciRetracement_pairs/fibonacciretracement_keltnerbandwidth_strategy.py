import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
