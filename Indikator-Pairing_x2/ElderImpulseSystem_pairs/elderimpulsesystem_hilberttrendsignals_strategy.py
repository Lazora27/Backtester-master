import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
