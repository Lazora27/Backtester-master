import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DemandIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DemandIndex': 1.0
        })
    )
