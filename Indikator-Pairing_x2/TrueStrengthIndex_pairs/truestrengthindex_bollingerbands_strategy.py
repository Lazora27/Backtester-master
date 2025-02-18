import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
