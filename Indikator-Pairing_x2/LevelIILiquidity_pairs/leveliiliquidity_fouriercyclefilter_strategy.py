import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
