import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
