import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und Fisher
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'Fisher': 1.0
        })
    )
