import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AdaptiveATR': 1.0
        })
    )
