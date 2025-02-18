import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
