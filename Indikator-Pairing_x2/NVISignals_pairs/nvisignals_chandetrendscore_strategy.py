import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
