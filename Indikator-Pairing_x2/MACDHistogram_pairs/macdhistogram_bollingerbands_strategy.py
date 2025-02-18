import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'BollingerBands': 1.0
        })
    )
