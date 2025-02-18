import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'EaseOfMovement': 1.0
        })
    )
