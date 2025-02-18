import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HilbertPhaseIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HilbertPhaseIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HilbertPhaseIndicator': 1.0
        })
    )
