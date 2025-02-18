import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'IntradayIntensity': 1.0
        })
    )
