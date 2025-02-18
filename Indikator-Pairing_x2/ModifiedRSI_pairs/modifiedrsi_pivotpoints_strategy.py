import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PivotPoints': 1.0
        })
    )
