import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsEaseOfMovement_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsEaseOfMovement und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ArmsEaseOfMovement': 1.0,
            'EhlersDecycler': 1.0
        })
    )
