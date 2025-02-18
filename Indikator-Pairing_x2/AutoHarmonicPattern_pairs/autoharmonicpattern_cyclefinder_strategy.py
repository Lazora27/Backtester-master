import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'CycleFinder': 1.0
        })
    )
