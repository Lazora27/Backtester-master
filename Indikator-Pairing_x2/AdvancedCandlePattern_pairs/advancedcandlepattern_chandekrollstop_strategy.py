import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
