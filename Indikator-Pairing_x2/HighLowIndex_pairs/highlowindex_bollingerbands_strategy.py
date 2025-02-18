import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
