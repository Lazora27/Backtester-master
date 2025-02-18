import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
