import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
