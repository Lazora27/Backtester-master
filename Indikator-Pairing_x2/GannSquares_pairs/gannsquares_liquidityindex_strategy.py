import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'LiquidityIndex': 1.0
        })
    )
