import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FisherSignals': 1.0
        })
    )
