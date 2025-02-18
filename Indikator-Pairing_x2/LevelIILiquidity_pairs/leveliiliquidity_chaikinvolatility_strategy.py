import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
