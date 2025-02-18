import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'BollingerBands': 1.0
        })
    )
