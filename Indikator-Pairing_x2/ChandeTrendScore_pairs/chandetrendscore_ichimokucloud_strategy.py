import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'IchimokuCloud': 1.0
        })
    )
