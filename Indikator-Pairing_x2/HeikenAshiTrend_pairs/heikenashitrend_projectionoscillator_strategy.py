import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
