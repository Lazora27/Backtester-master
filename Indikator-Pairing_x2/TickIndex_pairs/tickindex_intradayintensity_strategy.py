import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
