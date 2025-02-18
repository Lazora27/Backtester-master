import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'CoppockCurve': 1.0
        })
    )
