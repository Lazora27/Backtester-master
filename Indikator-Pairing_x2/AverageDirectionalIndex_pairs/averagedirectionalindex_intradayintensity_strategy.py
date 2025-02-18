import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
