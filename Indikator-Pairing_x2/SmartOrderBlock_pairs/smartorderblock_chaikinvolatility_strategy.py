import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
