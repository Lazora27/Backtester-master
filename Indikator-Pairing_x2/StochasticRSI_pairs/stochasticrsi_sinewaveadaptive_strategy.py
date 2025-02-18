import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
