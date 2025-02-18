import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PivotPoints
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PivotPoints': 1.0
        })
    )
