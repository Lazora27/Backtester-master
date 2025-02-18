import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ExtensionProjections': 1.0
        })
    )
