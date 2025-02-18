import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
