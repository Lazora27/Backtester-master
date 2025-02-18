import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
