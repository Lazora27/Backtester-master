import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
