import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'FlowOfFunds': 1.0
        })
    )
