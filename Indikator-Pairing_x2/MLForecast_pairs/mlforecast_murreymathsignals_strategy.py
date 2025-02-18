import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
