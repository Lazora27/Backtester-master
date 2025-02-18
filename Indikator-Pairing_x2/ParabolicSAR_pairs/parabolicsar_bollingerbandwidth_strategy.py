import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
