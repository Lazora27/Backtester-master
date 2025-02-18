import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
