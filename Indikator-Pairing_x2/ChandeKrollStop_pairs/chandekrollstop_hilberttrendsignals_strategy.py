import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
