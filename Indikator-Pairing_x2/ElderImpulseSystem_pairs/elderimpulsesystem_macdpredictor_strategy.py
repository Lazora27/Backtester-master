import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MACDPredictor': 1.0
        })
    )
