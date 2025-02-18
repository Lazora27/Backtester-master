import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
