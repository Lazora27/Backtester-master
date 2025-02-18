import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'EaseOfMovement': 1.0
        })
    )
