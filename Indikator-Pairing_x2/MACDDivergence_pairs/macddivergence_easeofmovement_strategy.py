import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'EaseOfMovement': 1.0
        })
    )
