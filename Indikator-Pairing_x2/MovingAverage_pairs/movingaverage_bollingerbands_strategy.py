import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'BollingerBands': 1.0
        })
    )
