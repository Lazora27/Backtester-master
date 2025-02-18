import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolatilityIndex': 1.0
        })
    )
