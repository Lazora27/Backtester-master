import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
