import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'CenterOfGravity': 1.0
        })
    )
