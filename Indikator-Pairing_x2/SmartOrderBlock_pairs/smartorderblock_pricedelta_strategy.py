import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PriceDelta
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PriceDelta': 1.0
        })
    )
