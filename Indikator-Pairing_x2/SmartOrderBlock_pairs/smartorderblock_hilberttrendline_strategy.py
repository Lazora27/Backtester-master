import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HilbertTrendline': 1.0
        })
    )
