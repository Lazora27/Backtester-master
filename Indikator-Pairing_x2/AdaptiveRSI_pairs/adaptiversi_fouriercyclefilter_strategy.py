import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
