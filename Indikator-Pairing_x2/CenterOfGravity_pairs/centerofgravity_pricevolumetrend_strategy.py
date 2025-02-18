import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
