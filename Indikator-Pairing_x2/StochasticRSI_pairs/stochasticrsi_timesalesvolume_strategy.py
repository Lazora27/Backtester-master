import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
