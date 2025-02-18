import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DPOCycles': 1.0
        })
    )
