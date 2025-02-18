import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
