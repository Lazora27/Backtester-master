import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'IntradayIntensity': 1.0
        })
    )
