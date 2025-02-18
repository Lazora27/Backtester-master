import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
