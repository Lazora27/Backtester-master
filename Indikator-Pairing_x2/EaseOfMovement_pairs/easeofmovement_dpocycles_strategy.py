import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und DPOCycles
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'DPOCycles': 1.0
        })
    )
