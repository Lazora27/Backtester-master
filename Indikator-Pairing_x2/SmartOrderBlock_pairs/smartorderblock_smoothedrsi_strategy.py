import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SmoothedRSI': 1.0
        })
    )
