import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'IntradayIntensity': 1.0
        })
    )
