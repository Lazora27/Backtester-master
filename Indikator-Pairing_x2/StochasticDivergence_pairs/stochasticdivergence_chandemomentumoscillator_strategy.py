import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ChandeMomentumOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ChandeMomentumOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ChandeMomentumOscillator': 1.0
        })
    )
