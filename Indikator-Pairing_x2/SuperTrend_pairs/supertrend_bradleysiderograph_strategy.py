import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'BradleySiderograph': 1.0
        })
    )
