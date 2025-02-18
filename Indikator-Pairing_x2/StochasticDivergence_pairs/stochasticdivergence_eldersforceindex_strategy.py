import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'EldersForceIndex': 1.0
        })
    )
