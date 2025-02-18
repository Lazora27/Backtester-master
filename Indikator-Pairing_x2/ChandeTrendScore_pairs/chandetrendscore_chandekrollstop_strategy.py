import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
