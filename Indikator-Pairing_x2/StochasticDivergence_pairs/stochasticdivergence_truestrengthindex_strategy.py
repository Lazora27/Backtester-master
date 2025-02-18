import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
