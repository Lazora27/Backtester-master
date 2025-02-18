import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
