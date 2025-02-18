import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BradleySiderograph': 1.0
        })
    )
