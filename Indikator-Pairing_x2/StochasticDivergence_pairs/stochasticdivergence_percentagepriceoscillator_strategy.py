import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
