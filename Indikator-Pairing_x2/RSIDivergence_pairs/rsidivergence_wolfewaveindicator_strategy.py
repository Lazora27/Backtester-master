import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
