import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'KeltnerChannels': 1.0
        })
    )
