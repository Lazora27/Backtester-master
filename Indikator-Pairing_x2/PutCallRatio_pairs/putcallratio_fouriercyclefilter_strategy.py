import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
