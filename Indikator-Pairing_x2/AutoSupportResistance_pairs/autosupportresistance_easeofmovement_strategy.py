import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'EaseOfMovement': 1.0
        })
    )
