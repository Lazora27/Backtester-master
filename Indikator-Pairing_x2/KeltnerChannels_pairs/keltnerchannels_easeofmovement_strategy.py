import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'EaseOfMovement': 1.0
        })
    )
