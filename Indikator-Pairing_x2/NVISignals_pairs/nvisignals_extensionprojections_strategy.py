import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ExtensionProjections': 1.0
        })
    )
