import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'IntradayIntensity': 1.0
        })
    )
