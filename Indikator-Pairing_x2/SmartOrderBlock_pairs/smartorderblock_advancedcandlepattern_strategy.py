import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
