import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AverageTrueRange': 1.0
        })
    )
