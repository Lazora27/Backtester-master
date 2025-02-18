import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
