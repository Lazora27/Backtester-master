import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'IntradayIntensity': 1.0
        })
    )
