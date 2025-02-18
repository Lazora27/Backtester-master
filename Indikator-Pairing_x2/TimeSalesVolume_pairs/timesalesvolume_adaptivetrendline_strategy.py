import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
