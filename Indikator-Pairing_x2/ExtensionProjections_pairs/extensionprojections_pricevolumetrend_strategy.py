import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
