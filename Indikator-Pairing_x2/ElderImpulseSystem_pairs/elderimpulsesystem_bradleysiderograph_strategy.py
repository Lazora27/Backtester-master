import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BradleySiderograph': 1.0
        })
    )
