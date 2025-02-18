import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'IntradayIntensity': 1.0
        })
    )
