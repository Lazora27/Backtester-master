import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WeeklyCycle': 1.0
        })
    )
