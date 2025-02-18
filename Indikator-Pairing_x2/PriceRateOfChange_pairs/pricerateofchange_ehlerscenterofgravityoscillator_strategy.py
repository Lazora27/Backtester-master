import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
