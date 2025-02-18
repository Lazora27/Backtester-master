import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
