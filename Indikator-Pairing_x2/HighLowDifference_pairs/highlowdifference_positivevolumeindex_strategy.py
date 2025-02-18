import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
