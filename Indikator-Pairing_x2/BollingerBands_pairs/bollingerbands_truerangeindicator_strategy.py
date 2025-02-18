import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
