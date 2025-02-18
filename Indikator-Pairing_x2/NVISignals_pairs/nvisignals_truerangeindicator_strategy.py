import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
