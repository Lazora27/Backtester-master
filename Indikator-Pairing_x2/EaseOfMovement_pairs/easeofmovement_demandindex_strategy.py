import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und DemandIndex
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'DemandIndex': 1.0
        })
    )
