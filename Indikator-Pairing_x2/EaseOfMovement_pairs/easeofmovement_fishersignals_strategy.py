import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und FisherSignals
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'FisherSignals': 1.0
        })
    )
