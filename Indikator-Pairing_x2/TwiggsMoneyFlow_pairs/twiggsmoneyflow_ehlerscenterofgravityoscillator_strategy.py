import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwiggsMoneyFlow_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwiggsMoneyFlow und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'TwiggsMoneyFlow': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
