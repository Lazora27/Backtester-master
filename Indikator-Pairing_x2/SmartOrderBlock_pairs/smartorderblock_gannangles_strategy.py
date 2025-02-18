import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und GannAngles
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'GannAngles': 1.0
        })
    )
