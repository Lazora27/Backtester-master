import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'IchimokuCloud': 1.0
        })
    )
