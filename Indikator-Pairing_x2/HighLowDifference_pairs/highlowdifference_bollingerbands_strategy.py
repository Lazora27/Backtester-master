import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BollingerBands
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BollingerBands': 1.0
        })
    )
