import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'IntradayIntensity': 1.0
        })
    )
