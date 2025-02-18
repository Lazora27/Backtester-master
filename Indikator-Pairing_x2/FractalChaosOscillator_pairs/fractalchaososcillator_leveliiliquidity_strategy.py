import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
