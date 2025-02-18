import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'EaseOfMovement': 1.0
        })
    )
