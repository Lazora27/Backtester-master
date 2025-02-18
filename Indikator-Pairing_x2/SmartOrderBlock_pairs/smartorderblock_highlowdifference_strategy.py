import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HighLowDifference': 1.0
        })
    )
