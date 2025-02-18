import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
