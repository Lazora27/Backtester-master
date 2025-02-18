import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
