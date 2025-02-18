import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'EaseOfMovement': 1.0
        })
    )
