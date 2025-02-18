import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
