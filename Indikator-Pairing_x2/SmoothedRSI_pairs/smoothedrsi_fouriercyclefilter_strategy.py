import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
