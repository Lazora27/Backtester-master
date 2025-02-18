import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'BollingerBands': 1.0
        })
    )
