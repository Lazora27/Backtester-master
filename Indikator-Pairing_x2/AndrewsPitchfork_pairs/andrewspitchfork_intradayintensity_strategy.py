import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'IntradayIntensity': 1.0
        })
    )
