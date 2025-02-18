import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
