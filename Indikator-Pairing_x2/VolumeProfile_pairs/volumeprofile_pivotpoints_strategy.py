import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und PivotPoints
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'PivotPoints': 1.0
        })
    )
