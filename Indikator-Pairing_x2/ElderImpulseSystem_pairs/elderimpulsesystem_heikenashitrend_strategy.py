import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
