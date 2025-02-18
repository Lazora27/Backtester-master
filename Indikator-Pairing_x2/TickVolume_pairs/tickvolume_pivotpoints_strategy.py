import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PivotPoints': 1.0
        })
    )
