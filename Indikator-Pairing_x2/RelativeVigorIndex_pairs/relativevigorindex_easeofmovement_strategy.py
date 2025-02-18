import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
