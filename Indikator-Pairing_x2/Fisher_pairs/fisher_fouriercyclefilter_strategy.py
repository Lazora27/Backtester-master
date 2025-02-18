import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
