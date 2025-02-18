import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BollingerBands
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BollingerBands': 1.0
        })
    )
