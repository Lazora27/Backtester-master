import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
