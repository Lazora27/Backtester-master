import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
