import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AdaptiveATR': 1.0
        })
    )
