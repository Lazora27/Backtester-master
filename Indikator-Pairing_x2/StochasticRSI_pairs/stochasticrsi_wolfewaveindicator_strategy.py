import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
