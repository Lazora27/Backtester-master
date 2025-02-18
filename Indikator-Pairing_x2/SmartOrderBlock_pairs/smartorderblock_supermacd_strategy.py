import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SuperMACD
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SuperMACD': 1.0
        })
    )
