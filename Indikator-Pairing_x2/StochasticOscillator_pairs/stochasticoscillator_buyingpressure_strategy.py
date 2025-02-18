import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
