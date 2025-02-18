import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AAIISentiment': 1.0
        })
    )
