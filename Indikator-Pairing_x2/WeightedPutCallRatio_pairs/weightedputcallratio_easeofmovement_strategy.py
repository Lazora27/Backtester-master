import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'EaseOfMovement': 1.0
        })
    )
