import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und BollingerBands
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'BollingerBands': 1.0
        })
    )
