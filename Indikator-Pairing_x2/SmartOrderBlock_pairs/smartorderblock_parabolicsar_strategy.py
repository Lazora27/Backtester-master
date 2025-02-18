import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ParabolicSAR': 1.0
        })
    )
