import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
