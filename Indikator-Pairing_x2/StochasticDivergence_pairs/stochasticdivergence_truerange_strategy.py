import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TrueRange': 1.0
        })
    )
