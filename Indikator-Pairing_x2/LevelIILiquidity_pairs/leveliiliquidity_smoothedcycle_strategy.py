import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SmoothedCycle': 1.0
        })
    )
