import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
