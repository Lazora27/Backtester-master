import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
