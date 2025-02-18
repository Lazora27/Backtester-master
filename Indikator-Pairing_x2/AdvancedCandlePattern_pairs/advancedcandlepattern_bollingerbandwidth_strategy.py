import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
