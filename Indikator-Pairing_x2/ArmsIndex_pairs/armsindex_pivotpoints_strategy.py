import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
