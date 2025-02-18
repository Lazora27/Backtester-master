import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
