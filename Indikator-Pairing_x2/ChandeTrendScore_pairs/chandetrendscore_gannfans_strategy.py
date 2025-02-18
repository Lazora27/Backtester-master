import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und GannFans
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'GannFans': 1.0
        })
    )
