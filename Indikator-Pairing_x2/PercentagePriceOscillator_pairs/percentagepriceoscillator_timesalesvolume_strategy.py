import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
