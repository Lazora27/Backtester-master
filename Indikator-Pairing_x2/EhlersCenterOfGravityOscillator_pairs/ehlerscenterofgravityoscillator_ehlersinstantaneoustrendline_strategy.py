import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersCenterOfGravityOscillator_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersCenterOfGravityOscillator und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'EhlersCenterOfGravityOscillator': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
