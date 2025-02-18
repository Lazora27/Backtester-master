import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
