import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
