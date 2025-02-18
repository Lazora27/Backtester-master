import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
