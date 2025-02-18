import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'IntradayIntensity': 1.0
        })
    )
