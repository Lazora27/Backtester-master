import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TimeCycle': 1.0
        })
    )
