import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VortexIndicator': 1.0
        })
    )
