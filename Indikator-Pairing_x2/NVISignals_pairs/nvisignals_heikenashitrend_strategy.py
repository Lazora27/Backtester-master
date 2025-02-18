import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
