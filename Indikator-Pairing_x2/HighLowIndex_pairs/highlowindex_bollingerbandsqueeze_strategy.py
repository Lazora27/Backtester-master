import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
