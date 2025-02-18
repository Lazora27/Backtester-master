import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und Fisher
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'Fisher': 1.0
        })
    )
