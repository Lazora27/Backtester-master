import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FisherTransform
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FisherTransform': 1.0
        })
    )
