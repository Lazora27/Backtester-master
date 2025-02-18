import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
