import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MurreyMathLines': 1.0
        })
    )
