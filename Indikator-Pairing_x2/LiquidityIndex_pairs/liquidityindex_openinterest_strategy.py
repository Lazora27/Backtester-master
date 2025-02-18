import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
