import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'EhlersDecycler': 1.0
        })
    )
