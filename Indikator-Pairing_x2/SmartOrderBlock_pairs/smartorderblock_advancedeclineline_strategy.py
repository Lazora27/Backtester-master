import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
