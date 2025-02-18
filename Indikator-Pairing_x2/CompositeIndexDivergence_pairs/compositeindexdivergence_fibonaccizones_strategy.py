import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'FibonacciZones': 1.0
        })
    )
