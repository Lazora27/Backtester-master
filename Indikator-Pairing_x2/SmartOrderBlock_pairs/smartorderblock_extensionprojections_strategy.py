import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ExtensionProjections': 1.0
        })
    )
