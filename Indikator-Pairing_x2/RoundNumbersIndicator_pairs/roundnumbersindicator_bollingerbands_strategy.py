import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
