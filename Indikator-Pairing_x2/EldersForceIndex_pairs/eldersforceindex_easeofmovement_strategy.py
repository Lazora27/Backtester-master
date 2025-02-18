import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
