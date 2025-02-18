import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'UlcerIndex': 1.0
        })
    )
