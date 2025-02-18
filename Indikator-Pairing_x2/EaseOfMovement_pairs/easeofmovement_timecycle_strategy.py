import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und TimeCycle
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'TimeCycle': 1.0
        })
    )
