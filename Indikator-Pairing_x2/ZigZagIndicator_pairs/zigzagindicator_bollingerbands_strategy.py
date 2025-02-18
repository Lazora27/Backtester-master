import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
