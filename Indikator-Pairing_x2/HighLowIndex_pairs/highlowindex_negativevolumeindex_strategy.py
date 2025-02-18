import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
