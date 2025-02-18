import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'EaseOfMovement': 1.0
        })
    )
