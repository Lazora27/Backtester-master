import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'EaseOfMovement': 1.0
        })
    )
