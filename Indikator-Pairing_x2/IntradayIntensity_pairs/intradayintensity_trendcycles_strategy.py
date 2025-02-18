import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und TrendCycles
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'TrendCycles': 1.0
        })
    )
