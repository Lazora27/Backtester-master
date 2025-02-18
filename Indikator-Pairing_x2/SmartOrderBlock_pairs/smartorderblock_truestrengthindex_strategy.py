import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
