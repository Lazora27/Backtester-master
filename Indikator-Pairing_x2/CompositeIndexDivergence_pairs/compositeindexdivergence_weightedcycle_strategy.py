import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'WeightedCycle': 1.0
        })
    )
