import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
