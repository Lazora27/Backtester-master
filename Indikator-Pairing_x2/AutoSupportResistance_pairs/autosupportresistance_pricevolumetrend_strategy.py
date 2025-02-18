import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
