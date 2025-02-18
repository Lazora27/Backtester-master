import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HullMovingAverage': 1.0
        })
    )
