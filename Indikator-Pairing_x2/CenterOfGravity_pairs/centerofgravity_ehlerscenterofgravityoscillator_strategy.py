import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
