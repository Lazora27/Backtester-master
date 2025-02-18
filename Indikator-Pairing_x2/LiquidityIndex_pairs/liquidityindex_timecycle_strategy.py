import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
