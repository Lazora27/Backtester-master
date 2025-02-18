import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
