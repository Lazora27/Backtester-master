import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
