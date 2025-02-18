import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrend_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrend und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrend': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
