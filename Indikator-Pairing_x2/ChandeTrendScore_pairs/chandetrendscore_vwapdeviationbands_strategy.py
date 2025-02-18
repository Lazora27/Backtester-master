import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
