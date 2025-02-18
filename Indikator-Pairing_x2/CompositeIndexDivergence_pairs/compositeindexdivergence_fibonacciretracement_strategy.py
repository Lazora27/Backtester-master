import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
