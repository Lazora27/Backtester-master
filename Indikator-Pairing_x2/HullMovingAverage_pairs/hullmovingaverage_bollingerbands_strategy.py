import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und BollingerBands
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'BollingerBands': 1.0
        })
    )
