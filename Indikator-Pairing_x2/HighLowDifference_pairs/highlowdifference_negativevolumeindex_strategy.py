import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
