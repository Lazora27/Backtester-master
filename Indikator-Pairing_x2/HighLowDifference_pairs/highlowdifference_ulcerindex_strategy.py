import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'UlcerIndex': 1.0
        })
    )
