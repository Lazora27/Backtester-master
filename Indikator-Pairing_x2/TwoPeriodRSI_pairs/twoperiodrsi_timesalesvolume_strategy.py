import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
