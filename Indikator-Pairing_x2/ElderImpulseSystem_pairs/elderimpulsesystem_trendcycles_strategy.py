import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TrendCycles': 1.0
        })
    )
