import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PivotPoints
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PivotPoints': 1.0
        })
    )
