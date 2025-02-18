import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BarStrength
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BarStrength': 1.0
        })
    )
