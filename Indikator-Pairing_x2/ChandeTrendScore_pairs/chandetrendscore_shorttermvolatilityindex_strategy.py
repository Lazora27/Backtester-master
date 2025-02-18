import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
