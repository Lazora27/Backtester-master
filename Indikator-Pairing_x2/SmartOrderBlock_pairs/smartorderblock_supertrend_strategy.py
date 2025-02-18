import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SuperTrend
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SuperTrend': 1.0
        })
    )
