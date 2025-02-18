import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und CycleFinder
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'CycleFinder': 1.0
        })
    )
