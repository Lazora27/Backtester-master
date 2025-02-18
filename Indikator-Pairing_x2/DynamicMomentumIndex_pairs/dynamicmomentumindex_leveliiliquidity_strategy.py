import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
