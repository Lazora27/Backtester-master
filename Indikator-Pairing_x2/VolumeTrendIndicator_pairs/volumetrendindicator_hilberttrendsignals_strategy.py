import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
