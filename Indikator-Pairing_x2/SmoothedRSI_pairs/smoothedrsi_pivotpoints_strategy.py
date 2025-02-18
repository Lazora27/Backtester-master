import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und PivotPoints
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'PivotPoints': 1.0
        })
    )
