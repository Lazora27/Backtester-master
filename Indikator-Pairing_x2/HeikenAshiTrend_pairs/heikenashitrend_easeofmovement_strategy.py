import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'EaseOfMovement': 1.0
        })
    )
