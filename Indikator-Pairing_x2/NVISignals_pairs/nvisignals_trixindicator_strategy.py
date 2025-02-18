import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TRIXIndicator': 1.0
        })
    )
