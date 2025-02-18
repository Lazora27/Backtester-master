import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'IntradayIntensity': 1.0
        })
    )
