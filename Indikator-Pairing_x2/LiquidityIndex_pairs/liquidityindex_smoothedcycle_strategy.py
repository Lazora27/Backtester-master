import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
