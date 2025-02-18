import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'IntradayIntensity': 1.0
        })
    )
