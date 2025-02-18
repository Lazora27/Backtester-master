import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
