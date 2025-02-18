import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
