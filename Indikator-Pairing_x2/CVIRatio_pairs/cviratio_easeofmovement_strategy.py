import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'EaseOfMovement': 1.0
        })
    )
