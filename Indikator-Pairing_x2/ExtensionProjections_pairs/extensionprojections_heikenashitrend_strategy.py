import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
