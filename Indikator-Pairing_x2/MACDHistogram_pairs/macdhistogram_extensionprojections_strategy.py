import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ExtensionProjections': 1.0
        })
    )
