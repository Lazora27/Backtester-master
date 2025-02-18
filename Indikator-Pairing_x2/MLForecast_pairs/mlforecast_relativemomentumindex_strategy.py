import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
