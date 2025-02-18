import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CenterOfGravity': 1.0
        })
    )
