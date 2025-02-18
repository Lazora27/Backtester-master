import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
