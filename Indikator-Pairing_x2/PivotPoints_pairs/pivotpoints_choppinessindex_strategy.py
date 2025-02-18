import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
