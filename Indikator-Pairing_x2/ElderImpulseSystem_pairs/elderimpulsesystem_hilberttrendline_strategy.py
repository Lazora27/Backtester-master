import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HilbertTrendline': 1.0
        })
    )
