import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'LiquidityIndex': 1.0
        })
    )
