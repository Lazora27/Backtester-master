import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
