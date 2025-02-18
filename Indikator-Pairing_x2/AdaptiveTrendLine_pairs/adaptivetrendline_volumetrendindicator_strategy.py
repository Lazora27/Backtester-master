import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
