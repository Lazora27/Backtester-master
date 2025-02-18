import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
