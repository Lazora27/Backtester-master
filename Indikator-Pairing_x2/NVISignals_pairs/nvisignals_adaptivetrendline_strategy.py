import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
