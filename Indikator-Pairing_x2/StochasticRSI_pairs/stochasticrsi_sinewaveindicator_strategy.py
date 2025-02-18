import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
