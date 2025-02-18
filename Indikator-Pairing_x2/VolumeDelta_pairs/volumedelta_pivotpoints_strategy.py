import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und PivotPoints
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'PivotPoints': 1.0
        })
    )
