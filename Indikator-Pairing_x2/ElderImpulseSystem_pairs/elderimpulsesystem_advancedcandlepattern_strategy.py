import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
