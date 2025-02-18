import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'IntradayIntensity': 1.0
        })
    )
