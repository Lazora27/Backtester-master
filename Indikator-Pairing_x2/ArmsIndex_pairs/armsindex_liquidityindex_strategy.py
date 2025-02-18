import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
