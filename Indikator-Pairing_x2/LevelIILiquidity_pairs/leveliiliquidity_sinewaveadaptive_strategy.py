import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
