import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
