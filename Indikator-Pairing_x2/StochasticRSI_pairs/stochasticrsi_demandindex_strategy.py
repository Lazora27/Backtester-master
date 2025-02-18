import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und DemandIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'DemandIndex': 1.0
        })
    )
