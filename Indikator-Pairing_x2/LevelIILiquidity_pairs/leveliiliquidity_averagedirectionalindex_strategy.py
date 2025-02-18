import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
