import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'IchimokuCloud': 1.0
        })
    )
