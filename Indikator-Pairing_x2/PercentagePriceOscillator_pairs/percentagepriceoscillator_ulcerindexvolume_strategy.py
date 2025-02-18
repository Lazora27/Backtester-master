import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
