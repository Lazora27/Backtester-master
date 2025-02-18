import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MultiTimeframeTrendFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MultiTimeframeTrendFinder
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MultiTimeframeTrendFinder': 1.0
        })
    )
