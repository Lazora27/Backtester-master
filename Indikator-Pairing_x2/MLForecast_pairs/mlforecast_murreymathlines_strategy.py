import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MurreyMathLines': 1.0
        })
    )
