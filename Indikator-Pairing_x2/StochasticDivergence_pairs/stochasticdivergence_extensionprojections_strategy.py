import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ExtensionProjections': 1.0
        })
    )
