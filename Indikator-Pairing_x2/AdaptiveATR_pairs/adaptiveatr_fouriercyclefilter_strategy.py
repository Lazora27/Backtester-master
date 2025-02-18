import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
