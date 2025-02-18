import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TimeCycle': 1.0
        })
    )
