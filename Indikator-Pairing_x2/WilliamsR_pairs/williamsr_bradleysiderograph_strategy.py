import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BradleySiderograph': 1.0
        })
    )
