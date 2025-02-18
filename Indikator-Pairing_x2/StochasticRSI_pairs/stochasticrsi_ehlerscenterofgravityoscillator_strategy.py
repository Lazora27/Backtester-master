import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
