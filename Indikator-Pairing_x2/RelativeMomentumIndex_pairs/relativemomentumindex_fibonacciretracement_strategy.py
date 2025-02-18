import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
