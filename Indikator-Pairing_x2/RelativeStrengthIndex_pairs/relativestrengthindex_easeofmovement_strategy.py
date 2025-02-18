import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
