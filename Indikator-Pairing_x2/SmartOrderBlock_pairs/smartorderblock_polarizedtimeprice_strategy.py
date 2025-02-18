import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
