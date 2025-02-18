import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'EhlersDecycler': 1.0
        })
    )
