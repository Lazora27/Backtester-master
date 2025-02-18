import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CycleFinder': 1.0
        })
    )
