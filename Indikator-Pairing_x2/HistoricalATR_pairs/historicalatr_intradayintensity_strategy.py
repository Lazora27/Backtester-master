import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'IntradayIntensity': 1.0
        })
    )
