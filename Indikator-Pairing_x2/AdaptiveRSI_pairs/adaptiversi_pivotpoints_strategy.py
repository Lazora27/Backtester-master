import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und PivotPoints
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'PivotPoints': 1.0
        })
    )
