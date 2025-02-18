import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
