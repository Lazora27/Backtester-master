import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ConnorsRSI': 1.0
        })
    )
