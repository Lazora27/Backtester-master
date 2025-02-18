import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
