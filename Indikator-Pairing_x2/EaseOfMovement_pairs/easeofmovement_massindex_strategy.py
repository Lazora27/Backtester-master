import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und MassIndex
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'MassIndex': 1.0
        })
    )
