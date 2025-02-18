import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'BradleySiderograph': 1.0
        })
    )
