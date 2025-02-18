import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und MovingAverage
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'MovingAverage': 1.0
        })
    )
