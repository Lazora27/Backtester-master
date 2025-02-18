import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BollingerBands
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BollingerBands': 1.0
        })
    )
