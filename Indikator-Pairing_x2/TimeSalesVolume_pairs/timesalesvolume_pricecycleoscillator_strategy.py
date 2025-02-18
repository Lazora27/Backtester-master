import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
