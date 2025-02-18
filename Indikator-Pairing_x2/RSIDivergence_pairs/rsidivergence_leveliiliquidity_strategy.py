import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
