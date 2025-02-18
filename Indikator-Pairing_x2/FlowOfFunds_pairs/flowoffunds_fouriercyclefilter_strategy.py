import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
