import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentageVolumeOscillator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentageVolumeOscillator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'PercentageVolumeOscillator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
