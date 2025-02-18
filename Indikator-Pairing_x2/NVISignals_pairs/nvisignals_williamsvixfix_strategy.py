import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
