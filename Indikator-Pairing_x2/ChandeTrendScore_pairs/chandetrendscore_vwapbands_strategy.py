import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'VWAPBands': 1.0
        })
    )
