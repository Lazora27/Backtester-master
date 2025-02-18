import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MultiTimeframeTrendFinder_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MultiTimeframeTrendFinder und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MultiTimeframeTrendFinder': 1.0,
            'ModifiedATR': 1.0
        })
    )
