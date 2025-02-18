import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
