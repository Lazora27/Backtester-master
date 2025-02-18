import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SuperMACD
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SuperMACD': 1.0
        })
    )
