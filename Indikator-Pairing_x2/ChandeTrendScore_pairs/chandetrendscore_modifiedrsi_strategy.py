import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ModifiedRSI': 1.0
        })
    )
