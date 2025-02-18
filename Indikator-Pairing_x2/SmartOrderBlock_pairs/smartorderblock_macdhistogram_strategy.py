import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'MACDHistogram': 1.0
        })
    )
