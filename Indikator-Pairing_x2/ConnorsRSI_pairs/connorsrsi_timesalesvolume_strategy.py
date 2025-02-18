import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
