import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DOMDepth
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DOMDepth': 1.0
        })
    )
