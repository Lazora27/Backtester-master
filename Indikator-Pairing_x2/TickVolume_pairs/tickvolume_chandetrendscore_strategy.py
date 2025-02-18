import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
