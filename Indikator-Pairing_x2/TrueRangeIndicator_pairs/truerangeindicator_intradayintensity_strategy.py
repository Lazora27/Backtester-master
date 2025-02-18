import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'IntradayIntensity': 1.0
        })
    )
