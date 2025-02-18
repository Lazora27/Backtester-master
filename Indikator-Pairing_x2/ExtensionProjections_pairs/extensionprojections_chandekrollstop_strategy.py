import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
