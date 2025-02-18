import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TrueRange
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TrueRange': 1.0
        })
    )
