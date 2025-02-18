import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'EaseOfMovement': 1.0
        })
    )
