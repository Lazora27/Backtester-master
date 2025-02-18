import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'EaseOfMovement': 1.0
        })
    )
