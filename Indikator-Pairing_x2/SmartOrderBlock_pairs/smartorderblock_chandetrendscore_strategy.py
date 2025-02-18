import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
