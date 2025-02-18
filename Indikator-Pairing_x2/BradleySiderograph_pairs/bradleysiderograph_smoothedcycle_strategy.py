import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'SmoothedCycle': 1.0
        })
    )
