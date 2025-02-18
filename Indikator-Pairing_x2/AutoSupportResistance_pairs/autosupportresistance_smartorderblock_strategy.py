import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SmartOrderBlock_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SmartOrderBlock
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SmartOrderBlock': 1.0
        })
    )
