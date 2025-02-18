import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MACDHistogram': 1.0
        })
    )
