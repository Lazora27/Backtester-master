import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PriceSquawk': 1.0
        })
    )
