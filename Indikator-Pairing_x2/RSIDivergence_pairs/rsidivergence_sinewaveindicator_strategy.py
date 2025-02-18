import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
