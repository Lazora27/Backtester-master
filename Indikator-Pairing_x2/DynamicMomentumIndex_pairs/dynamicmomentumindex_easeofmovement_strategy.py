import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
