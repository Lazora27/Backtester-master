import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
