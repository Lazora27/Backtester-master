import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
