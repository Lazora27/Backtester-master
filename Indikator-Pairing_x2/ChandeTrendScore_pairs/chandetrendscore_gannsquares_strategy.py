import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und GannSquares
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'GannSquares': 1.0
        })
    )
