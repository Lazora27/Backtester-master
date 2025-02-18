import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'KDJIndicator': 1.0
        })
    )
