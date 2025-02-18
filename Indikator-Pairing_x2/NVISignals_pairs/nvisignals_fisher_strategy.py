import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und Fisher
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'Fisher': 1.0
        })
    )
