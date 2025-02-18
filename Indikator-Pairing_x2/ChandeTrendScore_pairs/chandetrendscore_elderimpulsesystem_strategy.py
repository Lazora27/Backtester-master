import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
