import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
