import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
