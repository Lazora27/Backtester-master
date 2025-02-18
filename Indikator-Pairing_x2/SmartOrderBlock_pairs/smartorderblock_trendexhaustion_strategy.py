import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TrendExhaustion': 1.0
        })
    )
