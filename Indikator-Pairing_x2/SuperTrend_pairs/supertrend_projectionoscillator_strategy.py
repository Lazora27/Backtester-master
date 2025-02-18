import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
