import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
