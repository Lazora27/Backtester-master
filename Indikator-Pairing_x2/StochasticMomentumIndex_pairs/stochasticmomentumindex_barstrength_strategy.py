import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'BarStrength': 1.0
        })
    )
