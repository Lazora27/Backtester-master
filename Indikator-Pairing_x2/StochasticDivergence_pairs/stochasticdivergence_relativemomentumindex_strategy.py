import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
