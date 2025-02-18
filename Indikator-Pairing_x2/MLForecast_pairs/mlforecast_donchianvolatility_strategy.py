import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DonchianVolatility': 1.0
        })
    )
