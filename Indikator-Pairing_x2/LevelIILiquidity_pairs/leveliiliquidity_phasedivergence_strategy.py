import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PhaseDivergence': 1.0
        })
    )
