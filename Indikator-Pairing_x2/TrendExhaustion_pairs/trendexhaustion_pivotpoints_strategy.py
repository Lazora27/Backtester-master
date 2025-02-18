import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PivotPoints': 1.0
        })
    )
