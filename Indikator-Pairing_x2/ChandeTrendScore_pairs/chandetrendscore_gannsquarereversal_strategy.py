import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'GannSquareReversal': 1.0
        })
    )
