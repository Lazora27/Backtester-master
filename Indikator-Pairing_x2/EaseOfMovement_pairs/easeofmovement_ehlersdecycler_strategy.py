import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'EhlersDecycler': 1.0
        })
    )
