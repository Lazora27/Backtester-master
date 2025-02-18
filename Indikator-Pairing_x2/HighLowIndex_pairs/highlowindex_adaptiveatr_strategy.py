import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
