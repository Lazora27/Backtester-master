import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und CCITurbo
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'CCITurbo': 1.0
        })
    )
