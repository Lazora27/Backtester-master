import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
