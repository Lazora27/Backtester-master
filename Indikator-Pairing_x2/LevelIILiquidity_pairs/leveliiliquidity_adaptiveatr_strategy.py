import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AdaptiveATR': 1.0
        })
    )
