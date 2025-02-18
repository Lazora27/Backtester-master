import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'EaseOfMovement': 1.0
        })
    )
