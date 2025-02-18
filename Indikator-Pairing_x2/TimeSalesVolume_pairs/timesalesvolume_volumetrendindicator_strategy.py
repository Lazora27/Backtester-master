import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
