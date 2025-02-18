import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
