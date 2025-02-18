import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
