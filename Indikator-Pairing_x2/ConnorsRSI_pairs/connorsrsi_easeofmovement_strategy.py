import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'EaseOfMovement': 1.0
        })
    )
