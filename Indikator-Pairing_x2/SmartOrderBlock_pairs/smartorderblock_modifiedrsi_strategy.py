import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ModifiedRSI': 1.0
        })
    )
