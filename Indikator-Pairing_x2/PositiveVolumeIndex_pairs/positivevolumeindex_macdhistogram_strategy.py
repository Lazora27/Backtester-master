import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
