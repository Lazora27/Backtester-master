import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
