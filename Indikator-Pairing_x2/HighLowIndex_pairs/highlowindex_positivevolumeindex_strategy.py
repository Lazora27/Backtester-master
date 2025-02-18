import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
