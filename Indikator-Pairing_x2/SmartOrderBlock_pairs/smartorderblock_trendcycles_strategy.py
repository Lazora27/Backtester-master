import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TrendCycles': 1.0
        })
    )
