import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'IntradayIntensity': 1.0
        })
    )
