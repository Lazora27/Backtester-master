import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
