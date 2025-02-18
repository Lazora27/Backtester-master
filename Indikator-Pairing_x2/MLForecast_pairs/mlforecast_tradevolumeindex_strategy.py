import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
