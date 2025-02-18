import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'BollingerBands': 1.0
        })
    )
