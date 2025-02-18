import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und PivotPoints
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'PivotPoints': 1.0
        })
    )
