import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
