import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
