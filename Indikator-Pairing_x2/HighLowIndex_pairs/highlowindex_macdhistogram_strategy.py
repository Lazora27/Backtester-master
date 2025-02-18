import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
