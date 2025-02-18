import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
