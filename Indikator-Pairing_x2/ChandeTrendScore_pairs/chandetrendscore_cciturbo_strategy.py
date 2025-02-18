import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'CCITurbo': 1.0
        })
    )
