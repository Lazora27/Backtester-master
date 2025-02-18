import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TapeReading
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TapeReading': 1.0
        })
    )
