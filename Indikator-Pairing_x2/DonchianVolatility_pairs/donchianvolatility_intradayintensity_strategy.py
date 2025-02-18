import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'IntradayIntensity': 1.0
        })
    )
