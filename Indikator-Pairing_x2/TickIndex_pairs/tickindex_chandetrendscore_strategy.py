import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
