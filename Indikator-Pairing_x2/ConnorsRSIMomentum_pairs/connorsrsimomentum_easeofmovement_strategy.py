import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSIMomentum_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSIMomentum und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ConnorsRSIMomentum': 1.0,
            'EaseOfMovement': 1.0
        })
    )
