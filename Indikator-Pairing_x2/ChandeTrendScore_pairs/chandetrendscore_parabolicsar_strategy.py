import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ParabolicSAR': 1.0
        })
    )
