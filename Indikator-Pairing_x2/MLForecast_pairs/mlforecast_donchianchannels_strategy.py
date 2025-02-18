import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DonchianChannels': 1.0
        })
    )
