import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'IntradayIntensity': 1.0
        })
    )
