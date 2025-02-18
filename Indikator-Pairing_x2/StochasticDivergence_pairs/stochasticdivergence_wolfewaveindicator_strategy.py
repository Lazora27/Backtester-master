import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
