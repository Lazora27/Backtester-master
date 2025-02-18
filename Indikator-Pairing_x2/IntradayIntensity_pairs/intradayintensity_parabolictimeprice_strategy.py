import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
