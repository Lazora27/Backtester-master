import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
