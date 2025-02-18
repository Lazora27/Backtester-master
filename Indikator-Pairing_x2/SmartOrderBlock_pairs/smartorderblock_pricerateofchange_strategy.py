import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
