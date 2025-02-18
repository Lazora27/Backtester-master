import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
