import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
