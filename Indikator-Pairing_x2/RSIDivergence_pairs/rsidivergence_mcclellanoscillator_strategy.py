import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'McClellanOscillator': 1.0
        })
    )
