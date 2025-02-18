import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MultiTimeframeTrendFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MultiTimeframeTrendFinder
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MultiTimeframeTrendFinder': 1.0
        })
    )
