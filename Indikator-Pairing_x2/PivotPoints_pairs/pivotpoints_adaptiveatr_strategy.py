import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AdaptiveATR': 1.0
        })
    )
