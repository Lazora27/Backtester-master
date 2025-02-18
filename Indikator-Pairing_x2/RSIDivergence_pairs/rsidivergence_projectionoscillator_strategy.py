import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
