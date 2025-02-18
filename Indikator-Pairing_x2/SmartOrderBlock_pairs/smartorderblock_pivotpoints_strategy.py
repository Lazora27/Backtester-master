import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PivotPoints
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PivotPoints': 1.0
        })
    )
