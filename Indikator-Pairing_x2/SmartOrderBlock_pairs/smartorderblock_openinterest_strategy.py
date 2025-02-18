import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und OpenInterest
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'OpenInterest': 1.0
        })
    )
