import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AccelerationBands': 1.0
        })
    )
