import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'HullMovingAverage': 1.0
        })
    )
