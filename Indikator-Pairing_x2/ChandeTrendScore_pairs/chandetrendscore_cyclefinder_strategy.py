import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'CycleFinder': 1.0
        })
    )
