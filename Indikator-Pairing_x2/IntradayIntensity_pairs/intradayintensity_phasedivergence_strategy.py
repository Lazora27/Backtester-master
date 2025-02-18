import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'PhaseDivergence': 1.0
        })
    )
