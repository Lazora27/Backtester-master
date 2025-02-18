import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'LiquidityIndex': 1.0
        })
    )
