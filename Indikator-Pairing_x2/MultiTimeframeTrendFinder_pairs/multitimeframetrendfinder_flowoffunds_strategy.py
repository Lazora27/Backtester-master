import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MultiTimeframeTrendFinder_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MultiTimeframeTrendFinder und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MultiTimeframeTrendFinder': 1.0,
            'FlowOfFunds': 1.0
        })
    )
