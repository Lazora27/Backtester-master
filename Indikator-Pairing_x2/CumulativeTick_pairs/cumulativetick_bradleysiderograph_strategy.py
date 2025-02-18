import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'BradleySiderograph': 1.0
        })
    )
