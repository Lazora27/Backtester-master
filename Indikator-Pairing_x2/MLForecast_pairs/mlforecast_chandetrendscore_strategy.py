import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
