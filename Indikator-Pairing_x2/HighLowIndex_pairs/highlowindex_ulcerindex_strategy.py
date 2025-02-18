import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
