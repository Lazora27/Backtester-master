import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SuperMACD': 1.0
        })
    )
