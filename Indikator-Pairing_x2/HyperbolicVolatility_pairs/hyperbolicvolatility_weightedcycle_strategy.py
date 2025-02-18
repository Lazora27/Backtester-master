import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'WeightedCycle': 1.0
        })
    )
