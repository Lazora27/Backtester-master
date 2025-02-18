import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
