import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
