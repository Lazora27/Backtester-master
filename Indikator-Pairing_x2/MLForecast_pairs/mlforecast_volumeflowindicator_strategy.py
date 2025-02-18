import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
