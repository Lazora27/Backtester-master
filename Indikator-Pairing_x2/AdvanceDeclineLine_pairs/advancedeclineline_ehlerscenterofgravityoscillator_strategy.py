import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
