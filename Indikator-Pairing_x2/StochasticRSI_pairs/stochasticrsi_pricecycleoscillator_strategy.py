import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
