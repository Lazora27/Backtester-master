import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BuyingPressure': 1.0
        })
    )
