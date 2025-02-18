import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'IntradayIntensity': 1.0
        })
    )
