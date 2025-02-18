import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'BradleySiderograph': 1.0
        })
    )
