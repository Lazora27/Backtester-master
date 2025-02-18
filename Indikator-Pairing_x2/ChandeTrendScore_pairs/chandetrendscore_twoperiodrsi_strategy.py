import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
