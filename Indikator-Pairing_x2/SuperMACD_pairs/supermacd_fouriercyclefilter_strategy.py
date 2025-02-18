import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
