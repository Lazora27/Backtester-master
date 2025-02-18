import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
