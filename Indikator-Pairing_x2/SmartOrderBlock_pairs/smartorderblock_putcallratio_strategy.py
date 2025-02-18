import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PutCallRatio': 1.0
        })
    )
