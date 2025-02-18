import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
