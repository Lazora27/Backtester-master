import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
