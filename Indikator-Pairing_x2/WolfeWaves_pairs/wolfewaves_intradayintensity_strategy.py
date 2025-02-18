import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'IntradayIntensity': 1.0
        })
    )
