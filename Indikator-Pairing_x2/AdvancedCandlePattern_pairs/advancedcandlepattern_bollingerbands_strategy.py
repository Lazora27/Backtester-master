import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'BollingerBands': 1.0
        })
    )
