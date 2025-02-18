import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
