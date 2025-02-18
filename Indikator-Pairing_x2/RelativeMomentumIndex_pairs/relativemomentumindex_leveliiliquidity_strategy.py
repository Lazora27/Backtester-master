import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
