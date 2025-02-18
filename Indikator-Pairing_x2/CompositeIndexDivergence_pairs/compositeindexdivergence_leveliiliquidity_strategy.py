import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
