import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'EaseOfMovement': 1.0
        })
    )
