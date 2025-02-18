import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
