import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
