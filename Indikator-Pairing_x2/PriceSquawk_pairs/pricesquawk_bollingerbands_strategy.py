import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BollingerBands
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BollingerBands': 1.0
        })
    )
