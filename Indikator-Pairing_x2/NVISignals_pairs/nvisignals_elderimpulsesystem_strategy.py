import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
