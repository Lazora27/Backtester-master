import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WilliamsR
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WilliamsR': 1.0
        })
    )
