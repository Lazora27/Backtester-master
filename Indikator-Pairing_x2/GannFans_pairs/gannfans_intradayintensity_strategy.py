import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'IntradayIntensity': 1.0
        })
    )
