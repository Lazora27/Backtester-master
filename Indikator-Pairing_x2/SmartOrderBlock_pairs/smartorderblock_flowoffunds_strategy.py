import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FlowOfFunds': 1.0
        })
    )
