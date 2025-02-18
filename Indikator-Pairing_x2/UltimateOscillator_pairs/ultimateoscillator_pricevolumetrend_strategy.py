import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
